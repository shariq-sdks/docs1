const authenticateUser  = require('../handlers/authenticate-user');
const handleUnknown     = require('../handlers/handle-unknown');
const healthcheck       = require('../handlers/healthcheck');
const processVersion    = require('../handlers/process-version');
const processLocale     = require('../handlers/process-locale');
const processServerType = require('../handlers/process-server-type');
const redirectToDefault = require('../handlers/redirect-to-default');
const renderDoc         = require('../handlers/render-doc');
const renderSpec        = require('../handlers/render-spec');

module.exports = function(app) {
  // Set up routing based on the following link.
  //
  //   https://github.com/expressjs/express/blob/master/examples/route-middleware/index.js
  //

  // The root path. This setup makes requests to the root path redirect
  // to the path specified by 'defaultPath' configuration property.
  app.get('/', redirectToDefault);

  // Healthcheck endpoint.
  app.get('/__healthz', healthcheck);

  // The path to get the API doc for a version, a server type and a
  // locale.
  app.get('/:locale/:serverType/:version',
    processLocale, processServerType, processVersion, authenticateUser, renderDoc);

  // The path to get the API spec for a version, a server type and a
  // locale.
  app.get('/:locale/:serverType/:version/spec',
    processLocale, processServerType, processVersion, authenticateUser, renderSpec);

  // Unknown paths with a locale. This setup is just for rendering
  // error in the locale.
  app.use('/:locale*', processLocale, handleUnknown);

  // Unknown paths. This setup is based on the official way of handling
  // 404 responses. See the following link for more details.
  //
  //   https://expressjs.com/en/starter/faq.html#how-do-i-handle-404-responses
  //
  app.use(handleUnknown);
};