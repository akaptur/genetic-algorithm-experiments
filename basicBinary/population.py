from individual import Individual

class Population(object):
    def __init__(self, size, initialize=False):
        self.individuals = []
        
        if initialize:
            for i in range(0, size):
                individual = Individual()
                individual.generate_individual()
                self.individuals.append(individual)
    
    
    def get_fittest(self, solution):
        return max(self.individuals, key=lambda i: i.get_fitness(solution))