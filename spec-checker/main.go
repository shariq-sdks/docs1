package main

import (
	"apispecchecker/processor"
	"fmt"
)

func main() {
	// Execute the job.
	err := doJob()

	// Show the error if the job failed.
	if err != nil {
		fmt.Println(err)
	}
}

func doJob() error {
	// Read options.
	options, err := processor.ParseOptions()
	if err != nil {
		return err
	}

	// Read the target API spec (yaml files) locally.
	spec, err := processor.ReadSpec(options)
	if err != nil {
		return err
	}

	// Get java models from the version of authlete-java-common that corresponds
	// to the target spec.
	javaModelMap, err := processor.ReadJavaModels(spec, options)
	if err != nil {
		return err
	}

	// Build results to show.
	results, err := processor.BuildResults(*javaModelMap, *spec.YamlModelMap, spec.Metadata)
	if err != nil {
		return err
	}

	// Print results.
	err = processor.PrintResults(results, spec.Metadata, options)
	if err != nil {
		return err
	}

	// No error.
	return nil
}
