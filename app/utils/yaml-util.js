const FileUtil = require('./file-util');
const yaml     = require('js-yaml');

const loadSync = function(path) {
  return loadYaml(FileUtil.readSync(path));
};

const loadYaml = function(file) {
  return file ? yaml.load(file) : null;
};

module.exports = {
  loadSync: loadSync
};