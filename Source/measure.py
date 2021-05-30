from note import Note

class Measure:
    def __init__(self):
        self.position = 0
        self.fitness_score = 0
        self.notes = [tuple]*4

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, pos):
        self.position = pos
    
    @property
    def fitness_score(self):
        return self.fitness_score
    
    @fitness_score.setter
    def fitness_score(self, score):
        self.fitness_score = score

    @property
    def notes(self):
        return self.notes

    @notes.setter
    def notes(self, list_of_notes):
        self.notes = list_of_notes
