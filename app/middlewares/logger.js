const pino              = require('pino');
const expressPinoLogger = require('express-pino-logger');
const config            = require('../config');

// Create a pino logger instance.
const logger = pino(
  { level: config.logLevel },
  pino.destination(`${__dirname}/../logger.log`)
);

// Create an express pino logger instance　and expose it.
module.exports = expressPinoLogger({ logger: logger });