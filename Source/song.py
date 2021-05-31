

class Song:
    def __init__(self):
        self.measures = []
    
    def format_string(self):
        return str([measure.format_string() for measure in self.measures])

    @property
    def measures(self):
        return self._measures

    @measures.setter
    def measures(self, list_of_measures):
        self._measures = list_of_measures
