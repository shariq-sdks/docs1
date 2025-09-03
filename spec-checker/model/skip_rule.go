package model

type SkipRule struct {
	Packages   []string            `yaml:"packages"`
	Models     []string            `yaml:"models"`
	Properties map[string][]string `yaml:"properties"`
}
