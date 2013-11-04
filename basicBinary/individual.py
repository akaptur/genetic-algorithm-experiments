from bitstring import BitArray
import fitness
from random import random

class Individual(object):
    def __init__(self):
        self._default_gene_length = 64
        self._fitness = 0
        self.genes = BitArray(bin="0" * self._default_gene_length)

    def generate_individual(self):
        genes = [int(round(random())) for i in range(self._default_gene_length)]
        self.genes = BitArray(genes)

    def get_fitness(self, solution):
        if self._fitness == 0:
            pairs = zip(self.genes, solution)
            self._fitness = sum(1 for gene, sol in pairs if gene == sol)

        return self._fitness
    
    def __str__(self):
        return self.genes.bin