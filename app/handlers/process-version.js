const config            = require('../config');
const NotFoundException = require('../exceptions/not-found-exception');

// A map holding the latest versions for each server type.
const LATEST_VERSION_MAP = Object.entries(config.supportedVersions).reduce(
  (prev, [k, v]) => { return { ...prev, [k]: v.at(-1) } }, {}
);

const createVersionInfo = function(version, latest) {
  return { version: version, latest: latest };
};

module.exports = function(req, res, next) {
  // If the version for the server type is supported.
  if (config.supportedVersions[req.params.serverType].includes(req.params.version))
  {
    // Create a version info.
    req.versionInfo =
      createVersionInfo(req.params.version, LATEST_VERSION_MAP[req.params.serverType] === req.params.version);

    // Pass control to the next process.
    return next();
  }

  // If the requested version is 'latest'.
  if (req.params.version === 'latest')
  {
    // Look up the latest version of the server type and then create a
    // version info.
    req.versionInfo =
      createVersionInfo(LATEST_VERSION_MAP[req.params.serverType], true);

    // Pass control to the next process.
    return next();
  }

  // The version for the server type is not supported.
  // Pass control to the error handler.
  next(new NotFoundException());
};