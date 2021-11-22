const config = require('../config');

module.exports = function(req, res, next) {
  // The latest version of the spec for the server type.
  const latestVersion = config.supportedVersions[req.params.serverType].at(-1);

  // Redirect to the path for the latest version of the spec.
  res.redirect(`/${req.params.locale}/${req.params.serverType}/${latestVersion}`);
};