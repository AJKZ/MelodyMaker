"""
Song class
Has a list of measures
Has a fitness score
"""

class Song:
    def __init__(self):
        self.measures = []
        self.fitness_score = 0
    

    def string_format(self):
        return str([measure.string_format() for measure in self.measures])


    def write_format(self):
        return [[    
                    note
                for measure in self.measures
            for note in measure.notes
        ]]


    @property
    def measures(self):
        return self._measures


    @measures.setter
    def measures(self, list_of_measures):
        self._measures = list_of_measures


    @property
    def fitness_score(self):
        return self._fitness_score
    
    
    @fitness_score.setter
    def fitness_score(self, score):
        self._fitness_score = score
