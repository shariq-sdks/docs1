package utils

import (
	"os"
	"regexp"
	"slices"
	"strings"

	"gopkg.in/yaml.v3"
)

// The pattern for camel case string.
var camelCaseRegex = regexp.MustCompile(`([a-z0-9])([A-Z])`)

// The pattern for converting camel-case to snake-case.
var camelToSnakePattern = `${1}_${2}`

// ReadFile reads the file at filePath and returns its contents as a
// string.
func ReadFile(filePath string) (string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return "", err
	}

	return string(data), nil
}

// ReadYaml reads a YAML file at filePath and unmarshals it into a value
// of type T. It returns the unmarshaled value or an error.
func ReadYaml[T any](filePath string) (T, error) {
	var zero T

	data, err := os.ReadFile(filePath)
	if err != nil {
		return zero, err
	}

	var result T
	err = yaml.Unmarshal(data, &result)
	if err != nil {
		return zero, err
	}

	return result, nil
}

// ToSnakeCase converts a camel-case string to a snake-case string.
func ToSnakeCase(input string) string {
	return strings.ToLower(
		camelCaseRegex.ReplaceAllString(input, camelToSnakePattern),
	)
}

// GetDiff returns the elements in present that does not exist in reference.
// If present is empty, it returns reference. If present is empty, it
// returns nil.
func GetDiff(present []string, reference []string) []string {
	if len(present) == 0 {
		return reference
	}

	if len(reference) == 0 {
		return nil
	}

	unknownElements := []string{}

	for _, e := range reference {
		if !slices.Contains(present, e) {
			unknownElements = append(unknownElements, e)
		}
	}

	return unknownElements
}
