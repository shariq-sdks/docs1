package processor

import (
	"apispecchecker/formatter"
	"apispecchecker/model"
	"fmt"
)

// PrintResults prints results using a specified formatter.
func PrintResults(
	results []*model.Result, specMetadata *model.SpecMetadata, options *model.Options) error {
	// Get a result formatter.
	formatter, err := getFormatter(options)
	if err != nil {
		return err
	}

	// Format the results with the formatter.
	output, err := formatter.Format(results, specMetadata, options)
	if err != nil {
		return err
	}

	// Show the formatted results.
	fmt.Print(output)

	// No error.
	return nil
}

func getFormatter(options *model.Options) (formatter.IFormatter, error) {
	// Return the specified formatter.
	switch options.Format {
	case "text":
		// The formatter for text.
		return &formatter.TextFormatter{}, nil
	default:
		// Invalid formatter.
		return nil, fmt.Errorf("invalid formatter type '%s'", options.Format)
	}
}
