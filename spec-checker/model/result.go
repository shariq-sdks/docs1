package model

type Result struct {
	JavaModel              *JavaModel
	YamlModel              *YamlModel
	UnknownModelProperties []string
	RemovedModelProperties []string
}
