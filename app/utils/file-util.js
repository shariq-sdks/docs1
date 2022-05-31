const fs = require('fs');

const readSync = function(path) {
  try
  {
    return fs.readFileSync(path, 'utf-8');
  }
  catch(e)
  {
    return handleError(e);
  }
};

const readAsync = async function(path) {
  try
  {
    return await fs.promises.readFile(path, 'utf-8');
  }
  catch(e)
  {
    return handleError(e);
  }
};

const handleError = function(error) {
  if (error.code === 'ENOENT')
  {
    // The target file was not found.
    return null;
  }

  // Rethrow the other errors.
  throw error;
};

module.exports = {
  readSync:  readSync,
  readAsync: readAsync
};