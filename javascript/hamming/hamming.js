var Hamming = function() {};

Hamming.prototype.compute = function(strand1, strand2) {
  var hDistance = 0;
  var strand1 = strand1.split('');
  var strand2 = strand2.split('');

  if (strand1.length !== strand2.length) { throw "DNA strands must be of equal length."; }

  for (var i = 0; i < strand1.length; i++) {
    if (strand1[i] !== strand2[i]) { hDistance++ };
  }

  return hDistance;
}

module.exports = Hamming;