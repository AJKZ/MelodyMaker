# #design
# #   sort of running function
# #   mutation function
# #   create children
# #   remember best child
# #   fitness function
# #   
# #
# from random import choices, randint, randrange, random, sample
# from typing import List, Callable, Tuple

# class genetic:


#     Genome = List[int]
#     Population = List[Genome]
    
#     def generateGenome(length:int) -> Genome:
#         return choices([0, 1], k=length)
        
#     def generatePopulation (size:int, genomeLength: int) -> Population:
#         return [generateGenome(genomeLength) for _ in range(size)]

#     def mutation (self, genome):
#         return None

#     def run (self):
#         return None

#     def createChild (self, number):
#         return number
    
#     def fitness(self, fitness):
#         return None
