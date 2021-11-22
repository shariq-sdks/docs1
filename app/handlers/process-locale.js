const config            = require('../config');
const NotFoundException = require('../exceptions/not-found-exception');

module.exports = function(req, res, next) {
  // Check if the locale is supported.
  if (config.supportedLocales.includes(req.params.locale))
  {
    // OK. The locale is supported.

    // Set the current locale to the requested locale. After this,
    // the current locale is used for rendering pages.
    req.currentLocale = req.params.locale;

    // Pass control to the next process.
    return next();
  }

  // The locale is not supported.
  // Pass control to the error handler.
  next(new NotFoundException('Locale not found.'));
};