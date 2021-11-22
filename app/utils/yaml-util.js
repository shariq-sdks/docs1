const fs   = require('fs');
const yaml = require('js-yaml');

const loadSync = function(path) {
  return loadYaml(readFileSync(path));
};

const loadAsync = async function(path) {
  return loadYaml(await readFileAsync(path));
};

const loadYaml = function(file) {
  return file ? yaml.load(file) : null;
};

const readFileSync = function(path) {
  try
  {
    return fs.readFileSync(path, 'utf-8');
  }
  catch(e)
  {
    return handleError(e);
  }
};

const readFileAsync = async function(path) {
  try
  {
    return await fs.promises.readFile(path, 'utf-8');
  }
  catch(e)
  {
    return handleError(e);
  }
};

const handleError = function(error) {
  if (error.code === 'ENOENT')
  {
    // The target file was not found.
    return null;
  }

  // Rethrow the other errors.
  throw error;
};

module.exports = {
  loadSync:  loadSync,
  loadAsync: loadAsync
};