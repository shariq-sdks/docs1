const config       = require('../config');
const ResponseUtil = require('../utils/response-util');

const isTryAllowed = function(req) {
  // When the requested server type is 'shared', we only enable 'TRY'
  // function on the API doc (Function of making test API calls from the
  // API doc to Authlete API) when the requested version is the latest one.
  // This is because it might cause inconsistent results if we allow API
  // calls from the older versions of the API doc to the shared Authlete
  // API due to version differences. For instance, let's say that the API
  // doc supports '2.2.0', '2.2.1' and '2.2.2' as its supported API versions
  // and the version of the deployed shared Authlete API is '2.2.2'.
  // In this case, it will be no problem to make API calls to the shared
  // Authlete API from the latest version of API doc ('shared/2.2.2')
  // but it might cause inconsistent results to make API calls from the
  // older versions of the API doc ('/shared/2.2.0', '/shared/2.2.1')
  // because of version differences in request/response parameters, API
  // availability, etc.
  if (req.params.serverType === 'shared')
  {
    // Check if the requested version is the latest one.
    return req.versionInfo.latest;
  }

  // The 'TRY' function is always enabled if the requested server type
  // is not 'shared'.
  return true;
}

module.exports = async function(req, res, next) {
  // Render the main view.
  ResponseUtil.ok(req, res, 'main', { config: config, req: req, allowTry: isTryAllowed(req) });
};