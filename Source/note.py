

class Note:
    def __init__(self, pitch, duration=4):
        self.pitch = pitch
        self.duration = duration

    @property
    def pitch(self):
        return self.pitch
    
    @pitch.setter
    def pitch(self, pitch):
        self.pitch = pitch

    @property
    def duration(self):
        return self.duration
    
    @duration.setter
    def duration(self, duration):
        self.duration = duration