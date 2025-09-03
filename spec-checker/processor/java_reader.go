package processor

import (
	"apispecchecker/model"
	"apispecchecker/utils"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"slices"
	"strings"
)

// The java file suffix.
const javaFileSuffix = ".java"

// These classes are not regarded as parent classes.
var skippedParentClassNames = []string{
	"ArrayList",
	"Enum",
	"LinkedHashMap",
	"RuntimeException",
}

// The metadata files.
var metadataFiles = []string{
	"package-info.java",
}

// ReadJavaModels java models contained in authlete-java-common and create
// a map containing JavaModel objects. It return the map or an error.
func ReadJavaModels(spec *model.Spec, options *model.Options) (*map[string]*model.JavaModel, error) {
	switched := false
	stashed := false
	originalBranch := ""

	// The cleanup function that is executed after the process of this function.
	defer func() {
		cleanup(options.AjcPath, switched, stashed, originalBranch)
	}()

	// 1. Get the current branch name.
	output, err := utils.RunGitCommand(options.AjcPath, "rev-parse", "--abbrev-ref", "HEAD")
	if err != nil {
		return nil, err
	}
	originalBranch = strings.TrimSpace(string(output))

	// 2. Git stash just in case.
	output, err = utils.RunGitStash(options.AjcPath)
	if err != nil {
		return nil, err
	}
	stashed = utils.IsStashed(output)

	// 3. Switch to a commit referenced by the tag for the target version
	// of authlete-java-common (detached HEAD).
	tag := fmt.Sprintf("tags/authlete-java-common-%s", spec.Metadata.AjcVersion)
	_, err = utils.RunGitCheckout(options.AjcPath, "--detach", tag)
	if err != nil {
		return nil, err
	}
	switched = true

	// 4. Load java models from the target version of authlete-java-common.
	javaModelMap := make(map[string]*model.JavaModel)
	ajcJavaDirPath := filepath.Join(options.AjcPath, "src/main/java")
	err = loadJavaModels(javaModelMap, ajcJavaDirPath, ajcJavaDirPath)
	if err != nil {
		return nil, err
	}

	// No error.
	return &javaModelMap, nil
}

func cleanup(ajcPath string, switched bool, stashed bool, originalBranch string) {
	// NOTE: Currently, we don't catch errors returned by the following
	// processes.
	if switched && originalBranch != "" {
		// Switch back to the original branch if necessary.
		utils.RunGitCheckout(ajcPath, originalBranch)
	}

	if stashed {
		// Pop the original changes if necessary.
		utils.RunGitStash(ajcPath, "pop")
	}
}

func loadJavaModels(
	javaModelMap map[string]*model.JavaModel, targetDirPath string, ajcJavaDirPath string) error {
	// Read entries from the directory.
	entries, err := os.ReadDir(targetDirPath)
	if err != nil {
		return err
	}

	// Handle each entry to update java model map.
	for _, entry := range entries {
		err := handleEachEntryForJavaModel(entry, javaModelMap, targetDirPath, ajcJavaDirPath)
		if err != nil {
			return err
		}
	}

	// No error.
	return nil
}

func handleEachEntryForJavaModel(
	entry os.DirEntry, javaModelMap map[string]*model.JavaModel, targetDirPath string,
	ajcJavaDirPath string) error {
	// The name of the entry.
	name := entry.Name()

	// The full path of the entry.
	fullPath := filepath.Join(targetDirPath, name)

	// If the entry is a directory, look into the directory.
	if entry.IsDir() {
		loadJavaModels(javaModelMap, fullPath, ajcJavaDirPath)
		return nil
	}

	// If the entry name does not end with ".java", skip this entry.
	if !strings.HasSuffix(name, javaFileSuffix) {
		return nil
	}

	// If the java file is a metadata file, return nil.
	if slices.Contains(metadataFiles, name) {
		return nil
	}

	// Extract the class name from the java file name.
	javaClassName := strings.TrimSuffix(name, javaFileSuffix)

	// Update the java map with the entry, which represents a java file.
	err := updateJavaModelMap(javaModelMap, "", javaClassName, fullPath, ajcJavaDirPath)
	if err != nil {
		return err
	}

	// No error.
	return nil
}

func updateJavaModelMap(
	javaModelMap map[string]*model.JavaModel, javaPackage string, javaClassName string, javaFilePath string,
	ajcJavaDirPath string) error {
	// Read the content of the java file.
	javaFileContent, err := utils.ReadFile(javaFilePath)
	if err != nil {
		return err
	}

	// Get the package of the java class if not provided.
	if len(javaPackage) == 0 {
		javaPackage, err = getPackage(javaClassName, javaFileContent)
		if err != nil {
			return err
		}
	}

	// Get the JavaModel object for the parent class. The value of parentClass
	// might be nil if no parent class is defined for the current model.
	parentClass, err := getParentClass(javaModelMap, javaFileContent, javaPackage, ajcJavaDirPath)
	if err != nil {
		return err
	}

	// Collect all properties from the current model and, if present, its
	// parent class.
	properties := collectProperties(javaFileContent, parentClass)

	// Update the output map for the current java model.
	fqdn := javaPackage + "." + javaClassName
	javaModelMap[fqdn] = &model.JavaModel{javaPackage, javaClassName, properties}

	// No error.
	return nil
}

func getPackage(javaClassName string, javaFileContent string) (string, error) {
	// Look up the package from the java file content.
	matched := buildPackageRegex().FindStringSubmatch(javaFileContent)
	if matched == nil {
		// No package is defined for the java class. This won't happen.
		return "", fmt.Errorf("'%s' has no package", javaClassName)
	}

	// The matched part.
	return matched[1], nil
}

func getParentClass(
	javaModelMap map[string]*model.JavaModel, javaFileContent string, javaPackage string,
	ajcJavaDirPath string) (*model.JavaModel, error) {
	// Extract the parent class name from the current java model content
	// if present.
	parentClassName := extractParentClassName(javaFileContent)

	// The class has no parent class.
	if len(parentClassName) == 0 {
		return nil, nil
	}

	// Some parent classes should be ignored.
	if slices.Contains(skippedParentClassNames, parentClassName) {
		return nil, nil
	}

	// Get the parent class package.
	parentClassPackage := getParentClassPackage(javaFileContent, javaPackage, parentClassName)

	// The FQDN of the parent class.
	parentClassFqdn := parentClassPackage + "." + parentClassName

	// Check if the parent class already exists in the map.
	parentClass, exists := javaModelMap[parentClassFqdn]
	if exists {
		return parentClass, nil
	}

	// Build the path to the java file for the parent class.
	parentJavaFilePath := buildJavaFilePath(parentClassPackage, parentClassName, ajcJavaDirPath)

	// Update the map with the parent class info.
	err := updateJavaModelMap(
		javaModelMap, parentClassPackage, parentClassName, parentJavaFilePath, ajcJavaDirPath)
	if err != nil {
		return nil, err
	}

	// Get the parent class info from the map and return it.
	return javaModelMap[parentClassName], nil
}

func extractParentClassName(javaFileContent string) string {
	// Extract the parent class name from the java file content.
	matched := buildParentClassRegex().FindStringSubmatch(javaFileContent)

	// If not matched, return an empty string.
	if matched == nil {
		return ""
	}

	// Return the matched part.
	return matched[1]
}

func getParentClassPackage(javaFileContent string, javaPackage string, parentClassName string) string {
	// Build the path to the parent class from an import if present.
	parentClassPackage := getParentClassPackageFromImport(javaFileContent, parentClassName)
	if len(parentClassPackage) > 0 {
		return parentClassPackage
	}

	// The parent class package should be same as javaPackage.
	return javaPackage
}

func getParentClassPackageFromImport(javaFileContent string, parentClassName string) string {
	// Find a line of importing the parent class in the java class content.
	matched := buildParentClassImportRegex(parentClassName).FindStringSubmatch(javaFileContent)

	// If not matched, return an empty string.
	if matched == nil {
		return ""
	}

	// Build the full path of the parent class.
	return matched[1]
}

func buildJavaFilePath(javaPackage string, className string, ajcJavaDirPath string) string {
	// Build the path to the java file for the class.
	// e.g. "/path/to/ajc-dir/src/main/java/com/authlete/common/dto/ApiResponse.java"
	return filepath.Join(
		ajcJavaDirPath, strings.ReplaceAll(javaPackage, ".", "/"), className,
	) + javaFileSuffix
}

func collectProperties(javaFileContent string, parentClass *model.JavaModel) []string {
	// The resultant properties.
	properties := []string{}

	// Extract lines containing "private" properties.
	privatePropertyLines := buildPrivateFieldRegex().FindAllStringSubmatch(javaFileContent, -1)

	// Append all the "private" properties.
	for _, line := range privatePropertyLines {
		properties = append(properties, line[2])
	}

	// Append all the parent's properties if necessary.
	if parentClass != nil {
		properties = append(properties, parentClass.Properties...)
	}

	// Return the collected properties.
	return properties
}

func buildPackageRegex() *regexp.Regexp {
	return regexp.MustCompile(`package\s(.+);`)
}

func buildParentClassRegex() *regexp.Regexp {
	return regexp.MustCompile(`\s*class.+extends\s(\w+)`)
}

func buildParentClassImportRegex(className string) *regexp.Regexp {
	return regexp.MustCompile(fmt.Sprintf(`import\s(com\.authlete\.common\..+)\.%s;`, className))
}

func buildPrivateFieldRegex() *regexp.Regexp {
	return regexp.MustCompile(`(?m)^\s*private\s([\w\[\]]+)\s([\w]+);$`)
}
