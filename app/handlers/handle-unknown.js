const NotFoundException = require('../exceptions/not-found-exception');

module.exports = function(req, res, next) {
  // The requested route is unknown.
  // Pass control to the error handler.
  next(new NotFoundException('unknown route called'));
};