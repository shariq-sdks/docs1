module.exports = function(req, res, next) {
  // If we get here then health is ok.
  res.status(200).send('OK');
};