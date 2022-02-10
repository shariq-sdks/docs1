const path     = require('path');
const YamlUtil = require('../utils/yaml-util');

const loadSpec = async function(req) {
  return await YamlUtil.loadAsync(getPathToSpec(req));
};

const getPathToSpec = function(req) {
  return path.join(__dirname, `../specs/${req.params.serverType}/${req.params.version}/${req.params.locale}.yaml`);
};

module.exports = {
  loadSpec: loadSpec
};