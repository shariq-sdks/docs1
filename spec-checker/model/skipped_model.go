package model

type SkippedModel struct {
	SkipAll    bool     `yaml:"skipAll"`
	Properties []string `yaml:"properties,omitempty"`
}
