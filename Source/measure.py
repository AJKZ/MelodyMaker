from note import Note

class Measure:
    def __init__(self):
        self.position = 0
        self.fitness_score = 0
        self.notes = [tuple]*4

    def format_string(self):
        return [note.format_string() for note in self.notes]

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
    
    @property
    def fitness_score(self):
        return self._fitness_score
    
    @fitness_score.setter
    def fitness_score(self, score):
        self._fitness_score = score

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, list_of_notes):
        self._notes = list_of_notes
