package processor

import (
	"apispecchecker/model"
	"apispecchecker/utils"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// The java file suffix.
const yamlFileSuffix = ".yaml"

// ReadSpec reads API doc specification yaml files and creates a Spec
// object based on that. It return the constructed Spec object or an error.
func ReadSpec(options *model.Options) (*model.Spec, error) {
	// Build a path to the base directory of the spec.
	baseSpecDirPath :=
		filepath.Join(options.ApiDocPath, "specs", options.ServerType, options.Version)

	// Read metadata of the target spec.
	specMetadata, err := readSpecMetadata(baseSpecDirPath)
	if err != nil {
		return nil, err
	}

	// Read yaml files.
	yamlModelMap, err := readYamlModels(baseSpecDirPath, options.Locale)
	if err != nil {
		return nil, err
	}

	// Create a Spec object.
	spec := model.Spec{
		options.ServerType,
		options.Version,
		options.Locale,
		specMetadata,
		yamlModelMap,
	}

	// No error.
	return &spec, nil
}

func readSpecMetadata(baseSpecDirPath string) (*model.SpecMetadata, error) {
	// The path to the '.metadata.yaml' file for the spec.
	path := fmt.Sprintf("%s/.metadata.yaml", baseSpecDirPath)

	// Read the '.metadata.yaml'.
	metadata, err := utils.ReadYaml[model.SpecMetadata](path)
	if err != nil {
		return nil, err
	}

	// No error.
	return &metadata, nil
}

func readYamlModels(baseDirPath string, locale string) (*map[string]*model.YamlModel, error) {
	// The resultant map to contain yaml file info.
	yamlModelMap := make(map[string]*model.YamlModel)

	// Load models.
	modelDirPath := fmt.Sprintf("%s/%s/model", baseDirPath, locale)
	err := loadYamlModels(modelDirPath, yamlModelMap)
	if err != nil {
		return nil, err
	}

	// Load request models.
	requestDirPath := fmt.Sprintf("%s/request", modelDirPath)
	err = loadYamlModels(requestDirPath, yamlModelMap)
	if err != nil {
		return nil, err
	}

	// Load response models.
	responseDirPath := fmt.Sprintf("%s/response", modelDirPath)
	err = loadYamlModels(responseDirPath, yamlModelMap)
	if err != nil {
		return nil, err
	}

	// No error.
	return &yamlModelMap, nil
}

func loadYamlModels(targetDirPath string, yamlModelMap map[string]*model.YamlModel) error {
	// Read entries from the directory.
	entries, err := os.ReadDir(targetDirPath)
	if err != nil {
		return err
	}

	// Handle each entry to update yaml model map.
	for _, entry := range entries {
		err := handleEachEntryForYamlModel(entry, targetDirPath, yamlModelMap)
		if err != nil {
			return err
		}
	}

	// No error.
	return nil
}

func handleEachEntryForYamlModel(
	entry os.DirEntry, targetDirPath string, yamlModelMap map[string]*model.YamlModel) error {
	// Ignore a directory entry.
	if entry.IsDir() {
		return nil
	}

	// The name of the yaml file.
	name := entry.Name()

	// If the entry name does not end with ".yaml", skip this entry.
	if !strings.HasSuffix(name, yamlFileSuffix) {
		return nil
	}

	// The yaml model name.
	modelName := strings.TrimSuffix(name, yamlFileSuffix)

	// The path of the yaml file.
	yamlPath := filepath.Join(targetDirPath, name)

	// Read the content of the yaml file.
	yamlContent, err := utils.ReadYaml[map[string]interface{}](yamlPath)
	if err != nil {
		return err
	}

	// Read the "properties" from the yaml file. This could return nil.
	properties := extractPropertiesFromYaml(yamlContent)

	// Update the map with the information about the yaml file.
	fqdn := toModelFqdn(targetDirPath, modelName)
	yamlModelMap[fqdn] = &model.YamlModel{Name: modelName, Properties: properties}

	// No error.
	return nil
}

func extractPropertiesFromYaml(yamlContent map[string]interface{}) []string {
	// Extract properties from the yaml content.
	rawProperties := yamlContent["properties"]

	if rawProperties == nil {
		// No properties in the yaml content.
		return nil
	}

	// Extract property names defined in the "properties" object.
	return toNames(rawProperties.(map[string]interface{}))
}

func toNames(properties map[string]interface{}) []string {
	// The resultant array.
	names := make([]string, 0, len(properties))

	// Append each property name.
	for name := range properties {
		names = append(names, name)
	}

	return names
}

func toModelFqdn(targetDirPath string, modelName string) string {
	// The index of the first slash of "/model" in targetDirPath.
	idx := strings.Index(targetDirPath, "/model")

	// The part starting with "/model" in the targetDirPath.
	// For example, the part value is "/model/request".
	part := targetDirPath[idx:]

	// The map key (e.g. "/model/request/authorization_request").
	return part + "/" + modelName
}
