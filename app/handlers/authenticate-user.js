const basicAuth             = require('basic-auth');
const config                = require('../config');
const UnauthorizedException = require('../exceptions/unauthorized-exception');

// Server types that require user authentication.
const PROTECTED_SERVER_TYPES = [ 'dedicated', 'onpremise' ];

const isAuthenticationRequired = function(req) {
  return PROTECTED_SERVER_TYPES.includes(req.params.serverType);
};

const isAuthenticated = function(req) {
  // Extract the user credentials from the request.
  const requested = basicAuth(req);

  // Expected user credentials for the server type.
  const expected = config.credentials[req.params.serverType];

  // Verify the user credentials.
  return requested &&
         requested.name === expected.username &&
         requested.pass === expected.password
};

module.exports = function(req, res, next) {
  if (!isAuthenticationRequired(req))
  {
    // Authentication is not required.
    // Pass control to the next process.
    return next();
  }

  if (isAuthenticated(req))
  {
    // OK. The end-user is authenticated.
    // Pass control to the next process.
    return next();
  }

  // The end-user is not authenticated.
  // Pass control to the error handler.
  next(new UnauthorizedException('End-user is not authenticated.'));
};