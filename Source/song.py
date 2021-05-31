

class Song:
    def __init__(self):
        self.measures = []
    
    def string_format(self):
        return str([measure.string_format() for measure in self.measures])

    @property
    def measures(self):
        return self._measures

    @measures.setter
    def measures(self, list_of_measures):
        self._measures = list_of_measures
