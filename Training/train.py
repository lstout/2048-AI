# ******************************** #
# Double pole balancing experiment #
# ******************************** #
import math
import random
from neat import config, population, chromosome, genome, visualize
from simulator import Simulator

def evaluate_population(population):

	#evaluation function for the population
	simulation = Simulator(population)
	simulation.run()

def main():
	#create config
	config.load('2048_config')

	# neuron model type
	chromosome.node_gene_type = genome.NodeGene

	population.Population.evaluate = evaluate_population
	pop = population.Population()
	pop.epoch(1, save_best=1)

	winner = pop.stats[0][-1]

	print winner

if __name__ == "__main__":
	main()

