const translations = require('../translations');

const ok = function(req, res, view, locals) {
  return render(req, setupResponse(res, 200), view, locals);
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

const setupResponse = function(res, status) {
  return res
    .status(status)
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
  unauthorized:        unauthorized,
  notFound:            notFound,
  internalServerError: internalServerError
};