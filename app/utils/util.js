const fromArrayToObject = function(array, callback) {
  return array && callback ? Object.fromEntries(array.map(callback)) : null;
};

module.exports = { fromArrayToObject: fromArrayToObject };