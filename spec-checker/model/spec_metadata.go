package model

type SpecMetadata struct {
	AjcVersion string   `yaml:"ajcVersion"`
	SkipRule   SkipRule `yaml:"skipRule"`
}
