const ResponseUtil = require('../utils/response-util');
module.exports = async function (req, res, next) {
  ResponseUtil.ok(req, res, 'main', { oauthCallback: true });
};