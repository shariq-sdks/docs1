// Application configuration.
const config = {};

// Supported locales.
config.supportedLocales = [ 'en' ];

// Supported server types.
config.supportedServerTypes = [ 'shared' ];

// Supported API document versions for each server type.
config.supportedVersions = {
  shared: [ '2.2.19' ]
};

// The default locale.
config.defaultLocale = 'en';

// The URL path to which end-users are redirected when accessing the
// application root path ('/').
config.defaultPath = 'en/shared/latest';

// The port this application runs on.
config.port = process.env.PORT;

// The credentials required for accessing protected information.
config.credentials = {
  dedicated: { username: process.env.USERNAME_DEDICATED, password: process.env.PASSWORD_DEDICATED },
  onpremise: { username: process.env.USERNAME_ONPREMISE, password: process.env.PASSWORD_ONPREMISE }
};

// Log level.
config.logLevel = process.env.NODE_ENV === 'production' ? 'error' : 'info';

// Expose the custom configuration.
module.exports = config;