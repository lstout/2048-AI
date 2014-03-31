from term2048.game import Game
from neat import nn
from math import log
import copy
import sys

MOVES = [1,2,3,4]

class Simulator(object):
	def __init__(self,population):
		self.population = population

	def run(self):
		for chromosome in self.population:
			net = nn.create_phenotype(chromosome)
			game = Game()
			while True:
				if game.board.won() or not game.board.canMove():
					break
				state = [log_2(item) for l in game.board.cells for item in l]
				print dir(net)
				sys.exit(1)
				action = [v if valid(game.board,i+1) else -1 for i,v in enumerate(net.pactivate(state))]
				move = action.index(max(action)) + 1
				game.incScore(game.board.move(move))
			score = game.score
			chromosome.fitness = score

def log_2(n):
	try:
		log_n = log(n,2)
	except:
		log_n = 0
	return log_n

def valid(board, m):
	if board.validMove(m):
		board_copy = copy.deepcopy(board)
		before = board_copy.cells
		board_copy.move(m)
		after = board_copy.cells
		if before == after:
			return True
	return False
