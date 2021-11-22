const config = require('../config');

module.exports = function(req, res, next) {
    // Set the current locale to the default locale.
    req.currentLocale = config.defaultLocale;

    // Pass control to the next process.
    next();
};