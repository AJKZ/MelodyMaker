

class Note:
    def __init__(self, pitch, duration=4):
        self.pitch = pitch
        self.duration = duration

    @classmethod
    def with_tuple(cls, tuple):
        return Note(tuple[0], tuple[1])

    def format_string(self):
        return (self.pitch, self.duration)
        
    @property
    def pitch(self):
        return self._pitch
    
    @pitch.setter
    def pitch(self, p):
        self._pitch = p

    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        self._duration = duration
