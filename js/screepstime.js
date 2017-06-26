
const time_factor = 1

module.exports.currentTimeStamp = function currentTimeStamp () {
  return Game.time * time_factor
}

module.exports.currentDateTime = function currentDateTime () {
  return new Date(Game.time * time_factor*1000);
}
