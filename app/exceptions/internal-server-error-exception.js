const HttpException = require('./http-exception');

class InternalServerErrorException extends HttpException
{
  constructor(message)
  {
    super(500, message);
  }
}

module.exports = InternalServerErrorException;