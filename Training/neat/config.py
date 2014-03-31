# sets the configuration parameters for NEAT
from ConfigParser import ConfigParser

def load(file):
    try:
        config_file = open(file,'r')
    except IOError:
        print 'Error: file %s not found!' %file
        raise
    else:

        # set class attributes
        # phenotype
        Config.input_nodes          =       16
        Config.output_nodes         =       4
        Config.hidden_nodes         =       100
        #print 'fully_connected:',parameters.get('phenotype', 'fully_connected')
        Config.fully_connected      =       1
        Config.max_weight           =       10
        Config.min_weight           =       -10
        Config.feedforward          =       0
        Config.nn_activation        =       'exp'
        Config.weight_stdev         =       0.9

        # GA
        Config.pop_size                 =   100
        Config.max_fitness_threshold    =   float('inf')
        Config.prob_addconn             =   0.05
        Config.prob_addnode             =   0.03
        Config.prob_mutatebias          =   0.20
        Config.bias_mutation_power      =   0.5
        Config.prob_mutate_weight       =   0.9
        Config.weight_mutation_power    =   1.5
        Config.prob_togglelink          =   0.01
        Config.elitism                  =   1

        # genotype compatibility
        Config.compatibility_threshold  =   3.0
        Config.compatibility_change     =   0.0
        Config.excess_coeficient        =   1.0
        Config.disjoint_coeficient      =   1.0
        Config.weight_coeficient        =   0.4

        # species
        Config.species_size         =   10
        Config.survival_threshold   =   0.2
        Config.old_threshold        =   30
        Config.youth_threshold      =   10
        Config.old_penalty          =   0.2 # always in (0,1)
        Config.youth_boost          =   1.2   # always in (1,2)
        Config.max_stagnation       =   15

class Config:

    # phenotype config
    input_nodes         = None
    output_nodes        = None
    hidden_nodes        = None
    fully_connected     = None
    max_weight          = None
    min_weight          = None
    feedforward         = None
    nn_activation       = None
    weight_stdev        = None

    # GA config
    pop_size                = None
    max_fitness_threshold   = None
    prob_addconn            = None
    prob_addnode            = None
    prob_mutatebias         = None
    bias_mutation_power     = None
    prob_mutate_weight      = None # dynamic mutation rate (future release)
    weight_mutation_power   = None
    prob_togglelink         = None
    elitism                 = None

    #prob_crossover = 0.7  # not implemented (always apply crossover)
    #prob_weightreplaced = 0.0 # not implemented

    # genotype compatibility
    compatibility_threshold = None
    compatibility_change    = None
    excess_coeficient       = None
    disjoint_coeficient     = None
    weight_coeficient       = None

    # species
    species_size        = None
    survival_threshold  = None    # only the best 20% for each species is allowed to mate
    old_threshold       = None
    youth_threshold     = None
    old_penalty         = None    # always in (0,1)
    youth_boost         = None    # always in (1,2)
    max_stagnation      = None