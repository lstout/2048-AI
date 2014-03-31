function AI(grid) {
  this.grid = grid;
  //Read NN from '../Training/?'
}

// performs a search and returns the best move
AI.prototype.getBest = function() {
  state = //getState from grid
  output = NN.activate(state)
  move = output.IndexOf(Math.max(output));
  return this.translate(move)
}

AI.prototype.translate = function(move) {
 return {
    0: 'up',
    1: 'right',
    2: 'down',
    3: 'left'
  }[move];
}

