const config = require('../config');

module.exports = function(req, res, next) {
  // Redirect to the default path.
  res.redirect(`${config.defaultPath}`);
};