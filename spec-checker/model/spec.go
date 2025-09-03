package model

type Spec struct {
	ServerType   string
	Version      string
	Locale       string
	Metadata     *SpecMetadata
	YamlModelMap *map[string]*YamlModel
}
