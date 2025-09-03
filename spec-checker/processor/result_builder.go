package processor

import (
	"apispecchecker/model"
	"apispecchecker/utils"
	"slices"
	"strings"
)

// BuildResults combines the given java mode map and yaml model map and
// then constructs a Result object. It return the constructed Result object
// or an error.
func BuildResults(
	javaModelMap map[string]*model.JavaModel, yamlModelMap map[string]*model.YamlModel,
	specMetadata *model.SpecMetadata) ([]*model.Result, error) {
	// Read the special mapping that associates yaml model names for its
	// corresponding java model name.
	nameMap, err := utils.ReadYaml[map[string][]string]("name-map.yaml")
	if err != nil {
		return nil, err
	}

	// The list of results.
	results := []*model.Result{}

	for javaClassFqdn, javaModel := range javaModelMap {
		// Skip the class if the java class package should be skipped.
		if slices.Contains(specMetadata.SkipRule.Packages, javaModel.Package) {
			continue
		}

		// Skip the class if the java class should be skipped.
		if slices.Contains(specMetadata.SkipRule.Models, javaClassFqdn) {
			continue
		}

		// Get the list of yaml model names for the java model name. e.g.
		// For "HskResponse",
		//   [
		//     "/model/response/hsk_get_response",
		//     "/model/response/hsk_create_response",
		//     "/model/response/hsk_delete_response"
		//   ]
		// will be returned.
		yamlModelFqdns := toYamlModelFqdns(javaClassFqdn, javaModel, nameMap)

		for _, yamlModelFqdn := range yamlModelFqdns {
			// Create a result for each pair of a java model and a yaml model.
			results = append(results, buildResult(
				javaClassFqdn, javaModel, yamlModelMap[yamlModelFqdn], specMetadata))
		}
	}

	// No error.
	return results, nil
}

func toYamlModelFqdns(
	javaClassFqdn string, javaModel *model.JavaModel, nameMap map[string][]string) []string {
	// Check the special name map first.
	// Note that a java class name can link to multiple model names. e.g.
	// For "HskResponse",
	//   [
	//     "/model/response/hsk_get_response",
	//     "/model/response/hsk_create_response",
	//     "/model/response/hsk_delete_response"
	//   ]
	// will be returned.
	if v, ok := nameMap[javaClassFqdn]; ok {
		return v
	}

	// Convert to the yaml model FQDN from the java model name.
	yamlModelFqdn := toYamlModelFqdn(javaModel.Name)

	// Return a string array containing it.
	return []string{yamlModelFqdn}
}

func toYamlModelFqdn(javaModelName string) string {
	// Convert the java model name (camel-case) to a snake-case name.
	yamlModelName := utils.ToSnakeCase(javaModelName)

	// If the model is a request model.
	if strings.HasSuffix(yamlModelName, "request") {
		return "/model/request/" + yamlModelName
	}

	// If the model is a response model.
	if strings.HasSuffix(yamlModelName, "response") {
		return "/model/response/" + yamlModelName
	}

	// If the model is neither a request model or response model, it's
	// for a regular model e.g. access_token.
	return "/model/" + yamlModelName
}

func buildResult(
	javaClassFqdn string, javaModel *model.JavaModel, yamlModel *model.YamlModel,
	specMetadata *model.SpecMetadata) *model.Result {
	// Construct a Result object.
	result := &model.Result{javaModel, nil, nil, nil}

	// Update the result base on the corresponding yaml model if present.
	if yamlModel != nil {
		result.YamlModel = yamlModel
		result.UnknownModelProperties = getUnknownProperties(javaClassFqdn, javaModel, yamlModel, specMetadata)
		result.RemovedModelProperties = getRemovedProperties(javaModel, yamlModel)
	}

	// Return the result.
	return result
}

func getUnknownProperties(
	javaClassFqdn string, javaModel *model.JavaModel, yamlModel *model.YamlModel,
	specMetadata *model.SpecMetadata) []string {
	// Get the required properties from java properties by skipping unnecessary
	// properties.
	requiredJavaProperties := skipProperties(javaModel.Properties, specMetadata.SkipRule.Properties[javaClassFqdn])

	// Get properties that are present in the required java properties but
	// are not in the yaml properties.
	return utils.GetDiff(yamlModel.Properties, requiredJavaProperties)
}

func getRemovedProperties(javaModel *model.JavaModel, yamlModel *model.YamlModel) []string {
	// Get properties that are present in the yaml properties but are not
	// in the java properties.
	return utils.GetDiff(javaModel.Properties, yamlModel.Properties)
}

func skipProperties(properties []string, skips []string) []string {
	if len(skips) == 0 {
		// No properties to skip.
		return properties
	}

	var result []string

	for _, p := range properties {
		// Add the property only if it should not be skipped.
		if !slices.Contains(skips, p) {
			result = append(result, p)
		}
	}

	return result
}
