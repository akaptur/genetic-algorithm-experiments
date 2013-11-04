from bitstring import BitArray
import fitness
from random import random

class Individual(object):
    def __init__(self):
        self._default_gene_length = 64
        self._fitness = 0
        self.genes = BitArray()
        
        for i in range(0, self._default_gene_length):
            self.genes.bin += str('0')
        
    def generate_individual(self):
        self.genes = BitArray()
        
        for i in range(0, self._default_gene_length):
            gene = int(round(random()))
            self.genes.bin += str(gene)
        
    
    def get_fitness(self, solution):
        if self._fitness == 0:
            fitness = 0
            for i in range(0, len(self.genes)):
                if self.genes[i] == solution[i]:
                    fitness += 1

            self._fitness = fitness

        return self._fitness
    
    
    def __str__(self):
        return self.genes.bin