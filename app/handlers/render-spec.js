const memoizee          = require("memoizee");
const path              = require('path');
const NotFoundException = require('../exceptions/not-found-exception');
const FileUtil          = require('../utils/file-util');
const ResponseUtil      = require('../utils/response-util');

const getPathToSpec = function(serverType, version, locale) {
  return path.join(__dirname, `../specs/${serverType}/${version}/${locale}.yaml`);
};

const doGetSpec = async function(serverType, version, locale) {
  // Path to a specification file for the requested server type, version
  // and locale.
  const specPath = getPathToSpec(serverType, version, locale);

  // Read the specification file.
  const spec = await FileUtil.readAsync(specPath);

  if (!spec)
  {
    // The spec was not found.
    // NOTE: This won't happen as long as the spec resource is deployed
    // appropriately.
    throw new NotFoundException('spec was not found.');
  }

  return spec;
};

// Wrap 'doGetSpec' with 'memoizee' to enable cache mechanism. This means,
// after the first call to 'getSpec' with a server type, a version and
// a locale, the following calls to 'getSpec' with the server, the version
// and the locale will return the cached information.
const getSpec = memoizee(doGetSpec, { promise: true });

module.exports = async function(req, res, next) {
  let spec;

  try
  {
    // Get a specification file for the server type, version and the
    // locale.
    spec = await getSpec(
      req.params.serverType, req.versionInfo.version, req.params.locale);
  }
  catch (e)
  {
    // Failed to get the specification file.
    // Pass control to the error handler.
    return next(e);
  }

  // Respond with the specification file (yaml).
  ResponseUtil.okWithYaml(res, spec);
};