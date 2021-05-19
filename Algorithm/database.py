import glob as gl
import os
from os.path import dirname
import tomita.legacy.pysynth as ps

class database:

    def createDirectory (gen):
        parent_dir = "/" # should be set individually where you need to create dir
    # Path 
        path = os.path.join(parent_dir, gen) 
        try: 
            os.mkdir(path) 
        except OSError as error: 
            print(error) 
        print("Directory '% s' created" % gen) 
    
    def readFiles ():
        return None

database.createDirectory(1)
        



    # def createFile (self, song):
    #     for trackIndex, track in enumerate (song):
    #         ps.make_wav (
    #             track,
    #             bpm = 180,
    #             transpose = 1,
    #             pause = 0.0,
    #             boost = 1.3,
    #             repeat = 2,
    #             fn = self.getTrackFileName (trackIndex),
    #         )

    #     ps.mix_files (
    #         *[self.getTrackFileName (trackIndex) for trackIndex in range (len (song))],
    #         'song.wav'
    #     )

    #     for fileName in gl.glob ('track_*.wav'):
    #         os.remove (fileName)

    # def getTrackFileName (self, trackIndex):
    #     return f'track_{str (1000 + trackIndex) [1:]}.wav'
       