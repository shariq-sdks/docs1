const config            = require('../config');
const NotFoundException = require('../exceptions/not-found-exception');

// A cache object holding the latest versions for each server type.
const LATEST_VERSION_CACHE = {};

const getLatestVersion = function(serverType) {
  // Get the latest version for the server type from the cache.
  let latestVersion = LATEST_VERSION_CACHE[serverType];

  // If the cache doesn't have the latest version for the server type.
  if (!latestVersion)
  {
    // Read the latest version for the server type from the configuration.
    latestVersion = config.supportedVersions[serverType].at(-1);

    // Update the cache with it.
    LATEST_VERSION_CACHE[serverType] = latestVersion;
  }

  return latestVersion;
};

const isLatestVersion = function(serverType, version) {
  return getLatestVersion(serverType) === version;
};

const createVersionInfo = function(version, latest) {
  return { version: version, latest: latest };
};

module.exports = function(req, res, next) {
  // If the version for the server type is supported.
  if (config.supportedVersions[req.params.serverType].includes(req.params.version))
  {
    // Create a version info.
    req.versionInfo =
      createVersionInfo(req.params.version, isLatestVersion(req.params.serverType, req.params.version));

    // Pass control to the next process.
    return next();
  }

  // If the requested version is 'latest'.
  if (req.params.version === 'latest')
  {
    // Look up the latest version of the server type and then create a
    // version info.
    req.versionInfo =
      createVersionInfo(getLatestVersion(req.params.serverType), true);

    // Pass control to the next process.
    return next();
  }

  // The version for the server type is not supported.
  // Pass control to the error handler.
  next(new NotFoundException());
};