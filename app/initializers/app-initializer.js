const express           = require('express');
const routesInitializer = require('./routes-initializer');
const i18n              = require('../middlewares/i18n');
const logger            = require('../middlewares/logger');
const errorHandler      = require('../middlewares/error-handler');

module.exports = function(app) {
  // Set up view rendering engine.
  app.set('view engine', 'ejs');

  // Set up static files.
  app.use(express.static('public'));

  // Set up the logger.
  app.use(logger);

  // Set up a middleware for internationalization.
  app.use(i18n);

  // Set up routes.
  routesInitializer(app);

  // Set up a moddileware for error handling.
  app.use(errorHandler);
};