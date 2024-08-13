const renderDoc = require('../handlers/render-doc');
const renderSpec = require('../handlers/render-spec');
const renderOAuthCallback = require('../handlers/render-oauth-callback');

module.exports = async function (req, res, next) {
  const { handler = 'doc' } = req.params;
  switch (handler) {
    case 'doc':
      return renderDoc(req, res, next);
    case 'spec':
      return renderSpec(req, res, next);
    case 'oauth-callback':
      return renderOAuthCallback(req, res, next);
    default:
      return next();
  }
};