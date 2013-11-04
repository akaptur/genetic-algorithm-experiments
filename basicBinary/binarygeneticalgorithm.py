from bitstring import BitArray
from algorithm import Algorithm
from individual import Individual
from population import Population
import fitness


class BinaryGeneticAlgorithm(object):
    def __init__(self, sol, use_random_crossover=True):
        max_fitness = len(sol)
        generation_count = 0
        solution = BitArray(bin=sol)
        population = Population(50, initialize=True)
        
        while population.get_fittest(solution).get_fitness(solution) < max_fitness:
            print "Generation: %d" % (generation_count, )
            print "Fittest Scores: %d" % (population.get_fittest(solution).get_fitness(solution),)
            print "Fittest: %s\n" % (population.get_fittest(solution).genes.bin,)
            generation_count += 1
            population = Algorithm(use_random_crossover).evolvePopulation(population, solution)
        
        msg = "===== SOLUTION FOUND! =====\nGENERATION: %d\nGENES: %s\n"
        print msg % (generation_count, population.get_fittest(solution).genes.bin)
    
