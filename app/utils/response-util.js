const translations = require('../translations');

const ok = function(req, res, view, locals) {
  return render(req, setupResponse(res, 200), view, locals);
};

const okWithYaml = function(res, yaml) {
  return setupResponse(res, 200, 'text/yaml').send(yaml);
};

const unauthorized = function(req, res) {
  return render(req, setupResponse(res, 401).header('WWW-Authenticate', 'Basic'), 'errors/unauthorized');
};

const notFound = function(req, res) {
  return render(req, setupResponse(res, 404), 'errors/not-found');
};

const internalServerError = function(req, res) {
  return render(req, setupResponse(res, 500), 'errors/internal-server-error');
};

const setupResponse = function(res, status, contentType = 'text/html') {
  return res
    .status(status)
    .header('Content-Type', contentType)
    .header('Pragma', 'no-cache')
    .header('Cache-Control', 'no-cache, no-store, must-revalidate')
    .header('Expires', 0)
  ;
};

const render = function(req, res, view, locals) {
  return res.render(view, extendLocals(req, locals));
};

const extendLocals = function(req, locals) {
  return Object.assign(locals || {}, { translations: translations[req.currentLocale] });
};

module.exports = {
  ok:                  ok,
  okWithYaml:          okWithYaml,
  unauthorized:        unauthorized,
  notFound:            notFound,
  internalServerError: internalServerError
};