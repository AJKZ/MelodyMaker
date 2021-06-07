"""
Measure class
Has a position within a song
has a list of notes consisting of a tuple with:
    - the tone of the note
    - the length of the note
"""

class Measure:
    def __init__(self):
        self.position = 0
        # self.fitness_score = 0
        self.notes = []


    def string_format(self):
        return self._notes


    @property
    def position(self):
        return self._position


    @position.setter
    def position(self, pos):
        self._position = pos
    

    # @property
    # def fitness_score(self):
    #     return self._fitness_score
    

    # @fitness_score.setter
    # def fitness_score(self, score):
    #     self._fitness_score = score


    @property
    def notes(self):
        return self._notes


    @notes.setter
    def notes(self, list_of_notes):
        self._notes = list_of_notes
