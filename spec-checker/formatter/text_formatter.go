package formatter

import (
	"apispecchecker/model"
	"bytes"
	"html/template"
)

// outputTemplate is a template of output this formatter generates.
const outputTemplate = `
[Basic Info]

  API Doc: {{.Options.ApiDocPath}}
  API Server Type: {{.Options.ServerType}}
  API Version: {{.Options.Version}}
  API Locale: {{.Options.Locale}}
  Authlete Java Common: {{.Options.AjcPath}}

[Model Info]
{{- $specMetadata := .SpecMetadata -}}
{{- range .Results -}}
  {{- if hasDiff . }}

  Java Package: {{.JavaModel.Package}}
  Java Model Name: {{.JavaModel.Name}}
  	{{- if .YamlModel}}
  Yaml Model Name: {{.YamlModel.Name}}
	    {{- if .UnknownModelProperties}}
  [Unknown Properties]
	      {{- range .UnknownModelProperties}}
    - {{.}}
	      {{- end}}
	    {{- end}}
      {{- if .RemovedModelProperties}}
  [Removed Properties]
	      {{- range .RemovedModelProperties}}
    - {{.}}
		    {{- end}}
	    {{- end}}
    {{- else}}
  Unknown Model: {{.JavaModel.Name}}
	  {{- end}}
	{{- end}}
{{- end}}
`

// OutputTemplateData represents the data used in the template.
type OutputTemplateData struct {
	Options      *model.Options
	Results      []*model.Result
	SpecMetadata *model.SpecMetadata
}

// ModelSkipRule describes whether a model should be skipped entirely
// and which of its properties should be skipped.
type ModelSkipRule struct {
	SkipAll        bool
	SkipProperties []string
}

// TextFormatter formats results as human-readable text.
type TextFormatter struct{}

// Format generates a formatted string representation of the given results
// using the provided specification metadata and options. It builds and
// executes the output template with the given data and returns the result.
// If template building or execution fails, an error is returned.
func (f *TextFormatter) Format(
	results []*model.Result, specMetadata *model.SpecMetadata, options *model.Options) (string, error) {
	// Build an output template.
	tmpl, err := buildTemplate()
	if err != nil {
		return "", err
	}

	// The buffer for the output.
	var buf bytes.Buffer

	// The data used in the template.
	data := OutputTemplateData{
		Options:      options,
		Results:      results,
		SpecMetadata: specMetadata,
	}

	// Write the output data into the buffer.
	err = tmpl.Execute(&buf, data)
	if err != nil {
		return "", err
	}

	// No error.
	return buf.String(), nil
}

func buildTemplate() (*template.Template, error) {
	// Map of functions used in the template.
	funcMap := template.FuncMap{
		"hasDiff": hasDiff,
	}

	// Build an output template.
	return template.New("outputTemplate").Funcs(funcMap).Parse(outputTemplate)
}

func hasDiff(result *model.Result) bool {
	return result.YamlModel == nil ||
		len(result.UnknownModelProperties) > 0 ||
		len(result.RemovedModelProperties) > 0
}
