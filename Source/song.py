

class Song:
    def __init__(self):
        self.measures = []
    
    @property
    def measures(self):
        return self.measures

    @measures.setter
    def measures(self, list_of_measures):
        self.measures = list_of_measures
