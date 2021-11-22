const config            = require('../config');
const NotFoundException = require('../exceptions/not-found-exception');

module.exports = function(req, res, next) {
  // Check if the requested server type is supported.
  if (config.supportedServerTypes.includes(req.params.serverType))
  {
    // OK. The server type is supported.
    // Pass control to the next process.
    return next();
  }

  // The server type is not supported.
  // Pass control to the error handler.
  next(new NotFoundException());
};