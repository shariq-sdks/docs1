const config            = require('../config');
const NotFoundException = require('../exceptions/not-found-exception');

module.exports = function(req, res, next) {
  // Check if the version for the server type is supported.
  if (config.supportedVersions[req.params.serverType].includes(req.params.version))
  {
    // OK. The version for the server type is supported.
    // Pass control to the next process.
    return next();
  }

  // The version for the server type is not supported.
  // Pass control to the error handler.
  next(new NotFoundException());
};