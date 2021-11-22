const HttpException = require('./http-exception');

class NotFoundException extends HttpException
{
  constructor(message)
  {
    super(404, message);
  }
}

module.exports = NotFoundException;