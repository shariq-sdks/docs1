const InternalServerErrorException = require('../exceptions/internal-server-error-exception');
const NotFoundException            = require('../exceptions/not-found-exception');
const UnauthorizedException        = require('../exceptions/unauthorized-exception');
const ResponseUtil                 = require('../utils/response-util');

// Error handler. Exceptions passed by 'next(error)' are handled by this
// error handler. See the following link for more details.
//
//   https://expressjs.com/en/starter/faq.html#how-do-i-setup-an-error-handler
//
module.exports = function(err, req, res, next) {
  // Return an error response to the end-user based on the type of the
  // exception.
  switch (err.constructor)
  {
    case UnauthorizedException:
      // 401 error response.
      return ResponseUtil.unauthorized(req, res);

    case NotFoundException:
      // 404 error response.
      return ResponseUtil.notFound(req, res);

    case InternalServerErrorException:
    default:
      // Log the error.
      req.log.error(err);

      // 500 error response.
      return ResponseUtil.internalServerError(req, res);
  }
};