package processor

import (
	"apispecchecker/model"
	"flag"
	"fmt"
)

// ParseOptions parses command-line flags and returns a populated Options
// object. It validates the required fields and returns an error if any
// are missing.
func ParseOptions() (*model.Options, error) {
	// "ajc-path" (string):
	//   Specifies the path to the target authlete-java-common.
	ajcPath := flag.String(
		"ajc-path", "", "The base path of authlete-java-common (e.g. '/path/to/my-dir/authlete-java-common').")

	// "api-doc-path" (string):
	//   Specifies the path to the API doc directory.
	apiDocPath := flag.String(
		"api-doc-path", "", "The base path of the API doc directory (e.g. '/path/to/my-dir/new-api-doc').")

	// "server-type" (string):
	//   Specifies a target server type. (e.g. "shared")
	serverType := flag.String("server-type", "", "The target server type.")

	// "version" (string):
	//   Specifies a target API version. (e.g. "3.0.14")
	version := flag.String("version", "", "The target version.")

	// "locale" (string):
	//   Specifies a target locale. (e.g. "en")
	locale := flag.String("locale", "", "The target locale.")

	// "format" (string):
	//   Specifies the formatter used for formatting the results. (e.g.
	//   "text") Possible values is "text".
	format := flag.String(
		"format", "text", "The output format. Possible values is 'text'.")

	// Parse the options.
	flag.Parse()

	// Check the path to the target authlete-java-common.
	if len(*ajcPath) == 0 {
		return nil, fmt.Errorf("'ajc-path' option is required")
	}

	// Check the spec path.
	if len(*apiDocPath) == 0 {
		return nil, fmt.Errorf("'api-doc-path' option is required")
	}

	// Check the server type.
	if len(*serverType) == 0 {
		return nil, fmt.Errorf("'server-type' option is required")
	}

	// Check the API version.
	if len(*version) == 0 {
		return nil, fmt.Errorf("'version' option is required")
	}

	// Check the locale.
	if len(*locale) == 0 {
		return nil, fmt.Errorf("'locale' option is required")
	}

	// Create an Options object.
	options := model.Options{
		AjcPath:    *ajcPath,
		ApiDocPath: *apiDocPath,
		ServerType: *serverType,
		Version:    *version,
		Locale:     *locale,
		Format:     *format,
	}

	return &options, nil
}
