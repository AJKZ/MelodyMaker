import glob as gl
import os
import shutil
import ast
import tomita.legacy.pysynth as ps
# import tomita.legacy.pysynth as ps
# path in methods should be treated that, folder of python file is home folder 

class database:
    parent_dir =  os.getcwd()

    def createDirectory (self, gen):
        name = str(gen)
    # Path 
        path = os.path.join(database.parent_dir, name) 

        if(os.path.exists(path)):
            print("Directory exists, removing old one") 
            shutil.rmtree(path)
        
        os.mkdir(path) 

        print("Directory '% s' created" % name) 
    
    def createFile (self, path, data, name):
        if ".wav" in path:
            database.createWave(self,data)
            return
        try:
            os.remove(database.parent_dir+ path)
        except OSError:
            print("removing old file, and creating new one")

        f = open(database.parent_dir+ path, "w+")
        f.write("(")
        for bar in data:
            f.write('(')
            for note in bar:
                f.write(str(note))
                f.write(',')
            f.write('),')
        f.write(")")

    def readFile (self,name):
        with open(database.parent_dir + name) as f:
            file = eval(f.read())

        return file

    def createWave (self, song):
        for trackIndex, track in enumerate (song):
            ps.make_wav (
                track,
                bpm = 180,
                transpose = 1,
                pause = 0.0,
                boost = 1.3,
                repeat = 1,
                fn = self.getTrackFileName (trackIndex),
            )
        
        ps.mix_files (
            *[self.getTrackFileName (trackIndex) for trackIndex in range (len (song))],
            'song.wav'
        )

        for fileName in gl.glob ('track_*.wav'):
            os.remove (fileName)

    def getTrackFileName (self, trackIndex):  
        return f'track_{str (1000 + trackIndex) [1:]}.wav'

# Database = database()
# Database.createDirectory("k")
# Database.createFile("\k\iets.wav",Database.bach, "bach")        
# Database.createDirectory("One")
# Database.createFile("\One\iets.txt", Database.bach, "bach")
# p = Database.readFile("\One\iets.txt")

# Database.createFile("\One\iets.wav", p, "bach")
# Database.playsound("\One\iets.wav")
