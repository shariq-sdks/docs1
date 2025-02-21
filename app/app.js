const express        = require('express');
const config         = require('./config');
const appInitializer = require('./initializers/app-initializer');

// Create an application.
const app = express();

// Initialize the application.
appInitializer(app);

// Start the application.
app.listen(config.port);