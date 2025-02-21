const authenticateUser         = require('../handlers/authenticate-user');
const handleUnknown            = require('../handlers/handle-unknown');
const healthcheck              = require('../handlers/healthcheck');
const processVersion           = require('../handlers/process-version');
const processLocale            = require('../handlers/process-locale');
const processServerType        = require('../handlers/process-server-type');
const redirectToDefault        = require('../handlers/redirect-to-default');
const redirectToEnSharedLatest = require('../handlers/redirect-to-en-shared-latest');
const renderHandler            = require('../handlers/render');

module.exports = function (app) {
  // Set up routing based on the following link.
  //
  //   https://github.com/expressjs/express/blob/master/examples/route-middleware/index.js
  //

  // The root path. This setup makes requests to the root path redirect
  // to the path specified by 'defaultPath' configuration property.
  app.get('/', redirectToDefault);

  // Healthcheck endpoint.
  app.get('/__healthz', healthcheck);

  // Redirect requests to '/en/beta/3.0.0' to '/en/shared/latest'.
  app.get('/en/beta/3.0.0', redirectToEnSharedLatest);

  // The most common endpoint. Process the locale, server type, version,
  // and the render handler.
  app.get('/:locale/:serverType/:version/:handler?',
    processLocale, processServerType, processVersion, authenticateUser, renderHandler);

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