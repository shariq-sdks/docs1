package formatter

import (
	"apispecchecker/model"
)

// IFormatter defines the interface for formatting validation results
// into a human-readable string (e.g., text). Implementations are responsible
// for deciding how results are rendered and may support multiple output
// formats.
//
// Typical implementations might include:
//   - TextFormatter: renders results in plain text.
//
// The interface allows the formatting strategy to be swapped without
// affecting the core processing logic.
type IFormatter interface {
	// Format takes the set of results to format along with specification
	// metadata and command-line options, and returns the formatted output
	// as a string.
	//
	// Parameters:
	//   results:       A slice of Result objects that capture the comparison
	//                  between Java models and YAML models.
	//   specMetadata:  Metadata about the target API spec, including skip
	//                  rules.
	//   options:       Command-line options that may affect formatting
	//                  (e.g., output format type, verbosity).
	//
	// Returns:
	//   A string containing the formatted results, or an error if formatting
	//   fails.
	Format(
		results []*model.Result, specMetadata *model.SpecMetadata, options *model.Options,
	) (string, error)
}
