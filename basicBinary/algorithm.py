from individual import Individual
from population import Population
from random import random, uniform


class Algorithm(object):
    def __init__(self, use_random_crossover=False):
        self.uniform_rate = 0.5
        self.mutation_rate = 0.015
        self.tournament_size = 5
        self.elitism = True
        self.use_random_crossover = use_random_crossover
    
    def evolvePopulation(self, population, solution):
        population_size = len(population.individuals)
        new_population = Population(population_size, initialize=False)
        
        if self.elitism:
            new_population.individuals.append(population.get_fittest(solution))
        
        elitism_offset = 0
        if self.elitism:
            elitism_offset = len(new_population.individuals)
        
        for i in range(elitism_offset, population_size):
            individual_1 = self.tournament_selection(population, solution)
            individual_2 = self.tournament_selection(population, solution)
            
            if self.use_random_crossover:
                new_individual = self.crossover_random(individual_1, individual_2)
            else:
                new_individual = self.crossover_pt(individual_1, individual_2)
            
            new_population.individuals.append(new_individual)
        
        for i in range(elitism_offset, len(new_population.individuals)):
            self.mutate(new_population.individuals[i])
            
        return new_population


    def tournament_selection(self, population, solution):
        population_size = len(population.individuals)
        tournament = Population(self.tournament_size, False)
        
        for i in range(0, self.tournament_size):
            randomId = int(random() * population_size)
            tournament.individuals.append(population.individuals[randomId])
        
        return tournament.get_fittest(solution)


    def crossover_pt(self, individual_1, individual_2):
        crossover_individual = Individual()
        
        uniform_rate = uniform(3, 7) * .1
        crossover_point =  int(uniform_rate * len(crossover_individual.genes))
        
        crossover_individual.genes = individual_1.genes[0:crossover_point]
        crossover_individual.genes += individual_2.genes[crossover_point:]
        
        return crossover_individual


    def crossover_random(self, individual_1, individual_2):
        crossover_individual = Individual()
        
        for i in range(0, len(crossover_individual.genes)):
            # crossover
            if random() <= self.uniform_rate:
                crossover_individual.genes[i] = individual_1.genes[i]
            else:
                crossover_individual.genes[i] = individual_2.genes[i]
        
        return crossover_individual


    def mutate(self, individual):
        for i in range(0, len(individual.genes)):
            if random() <= self.mutation_rate:
                gene = int(round(random()))
                individual.genes[i] = gene