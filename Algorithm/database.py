import glob as gl
import os
import shutil
# import tomita.legacy.pysynth as ps
# path in methods should be treated that, folder of python file is home folder 
class database:
    parent_dir =  os.getcwd() # should be set individually where you need to create dir

    def createDirectory (gen):
        name = str(gen)

    # Path 
        path = os.path.join(database.parent_dir, name) 

        if(os.path.exists(path)):
            print("Directory exists, removing old one") 
            shutil.rmtree(path)
        
        os.mkdir(path) 

        print("Directory '% s' created" % name) 
    
    def createFile (path, name, data):
        try:
            os.remove(database.parent_dir+ name)
        except OSError:
            print("removing old file, and creating new one")

        f = open(database.parent_dir+ name, "w+")
        print(f)
        for i in data:
            line = ' '.join(str(x) for x in i)
            f.write(line + '\n')
            
    def readFile (name):
        print(database.parent_dir+ name, 'd')
        text = open(database.parent_dir +name)
        file = text.readlines()
        print(file)
        text.close()
        return file

database.createDirectory("one")
database.createFile("","\one\iets.txt",[('Apples', '=', 10), ('Oranges', '<', 20)])        
database.readFile( "\one\iets.txt")


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
       
