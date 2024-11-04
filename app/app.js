const express = require('express');
const config = require('./config');
const appInitializer = require('./initializers/app-initializer');

// Create an application.
const app = express();

app.use((req, res, next) => {
  if (req.path === '/en/beta/3.0.0') {
    return res.redirect(301, '/en/shared/latest');
  }
  next();
});

// Initialize the application.
appInitializer(app);

// Start the application.
app.listen(config.port);