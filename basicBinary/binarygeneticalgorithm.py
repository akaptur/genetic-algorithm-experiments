from bitstring import BitArray
from algorithm import Algorithm
from individual import Individual
from population import Population
import fitness


class BinaryGeneticAlgorithm(object):
    def __init__(self, sol, use_random_crossover=True):
        self.max_fitness = len(sol)
        self.generation_count = 0
        self.solution = BitArray(bin=sol)
        self.population = Population(50, initialize=True)
        self.use_random_crossover = use_random_crossover

    def go(self):
        while self.population.get_fittest(self.solution).get_fitness(self.solution) < self.max_fitness:
            print "Generation: %d" % (self.generation_count, )
            print "Fittest Scores: %d" % (self.population.get_fittest(self.solution).get_fitness(self.solution),)
            print "Fittest: %s\n" % (self.population.get_fittest(self.solution).genes.bin,)
            self.generation_count += 1
            self.population = Algorithm(self.use_random_crossover).evolvePopulation(self.population, self.solution)
        
        msg = "===== SOLUTION FOUND! =====\nGENERATION: %d\nGENES: %s\n"
        print msg % (self.generation_count, self.population.get_fittest(self.solution).genes.bin)
    
