// Application configuration.
const config = {};

// Supported locales.
config.supportedLocales = [ 'en' ];

// Supported server types.
config.supportedServerTypes = [ 'shared', 'dedicated' ];

// Supported API document versions for each server type.
config.supportedVersions = {
  shared: [ '2.2.19', '2.2.25', '2.2.30' ],
  dedicated : [ '2.3.0' ],
};

// The default locale.
config.defaultLocale = 'en';

// The URL path to which end-users are redirected when accessing the
// application root path ('/').
config.defaultPath = 'en/shared/latest';

// The port this application runs on.
config.port = process.env.PORT || '8080';

// The credentials required for accessing protected information.
config.credentials = {
  dedicated: { username: process.env.USERNAME_DEDICATED || 'ded', password: process.env.PASSWORD_DEDICATED || 'ded' },
  onpremise: { username: process.env.USERNAME_ONPREMISE || 'onp', password: process.env.PASSWORD_ONPREMISE || 'onp' }
};

config.isProduction = process.env.NODE_ENV === 'production'

// Log level.
config.logLevel = process.env.LOG_LEVEL || (config.isProduction ? 'error' : 'info');

// Log destination.
config.logDestination = process.env.LOG_DESTINATION;

// Expose the custom configuration.
module.exports = config;