const path     = require('path');
const config   = require('../config');
const Util     = require('../utils/util');
const YamlUtil = require('../utils/yaml-util');

const getPathToTranslation = function(locale) {
  return path.join(__dirname, `resources/${locale}.yaml`);
};

const loadTranslation = function(locale) {
  return YamlUtil.loadSync(getPathToTranslation(locale));
};

const loadTranslations = function(locales) {
  return Util.fromArrayToObject(locales, (l) => [l, loadTranslation(l)]);
};

// Load translations for the supported locales and expose it.
module.exports = loadTranslations(config.supportedLocales);