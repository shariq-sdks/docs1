const yaml              = require('js-yaml');
const NotFoundException = require('../exceptions/not-found-exception');
const ResponseUtil      = require('../utils/response-util');
const SpecUtil          = require('../utils/spec-util');

module.exports = async function(req, res, next) {
  // Load the specification for the requested server type, version and
  // locale.
  const spec = await SpecUtil.loadSpec(req);

  if (spec === null)
  {
    // The spec was not found.
    // NOTE: This won't happen as long as the spec resource is deployed
    // appropriately.

    // Pass control to the error handler.
    return next(new NotFoundException('spec was not found.'));
  }

  // Render the spec (yaml file).
  ResponseUtil.okWithYaml(res, yaml.dump(spec));
};