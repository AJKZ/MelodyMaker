import glob as gl
import os
import shutil
import tomita.legacy.pysynth as ps
# import tomita.legacy.pysynth as ps
# path in methods should be treated that, folder of python file is home folder 
bach = (
    (
        ('e', 8), ('f#', 8),
        ('g*', 4), ('f#', 8), ('e', 8), ('d#*', 4), ('e', 8), ('f#', 8),
        ('b3*', 4), ('c#', 8), ('d#', 8), ('e*', 4), ('d', 8), ('c', 8),
        ('b3*', 4), ('a3', 8), ('g3', 8), ('f#3*', 4), ('g3', 8), ('a3', 8),
        ('b3*', 8), ('a3', 8), ('g3', 8), ('f#3', 8), ('e3*', 4), ('e', 8), ('f#', 8),
        ('g*', 4), ('f#', 8), ('e', 8), ('d#*', 4), ('e', 8), ('f#', 8),
        ('b3*', 4), ('c#', 8), ('d#', 8), ('e*', 4), ('d', 8), ('c', 8),
        ('b3*', 4), ('a3', 8), ('g3', 8), ('g3*', 32), ('f#3*', 32), ('g3*', 32), ('f#3*', 32), ('g3*', 32), ('f#3*', 32), ('g3*', 32), ('f#3*', 6.4), ('g3', 8), ('g3*', -2),
    ),
    (
        ('g2', 8), ('f#2', 8),
        ('e2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
        ('g2*', 4), ('f#2', 4), ('e2', 4), ('f#2', 4),
        ('g2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
        ('g2*', 4), ('b2', 4), ('e2', 8), ('f#2', 8), ('g2', 8), ('f#2', 8),
        ('e2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
        ('g2*', 4), ('f#2', 4), ('e2', 4), ('f#2', 4),
        ('g2*', 4), ('c3', 4), ('d3', 4), ('d3', 4),
        ('b2*', -2),
    )
)
class database:
    
    parent_dir =  os.getcwd()

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
        if ".wav" in name:
            print("wav")
        print(name, 'name')
        try:
            os.remove(database.parent_dir+ name)
        except OSError:
            print("removing old file, and creating new one")

        f = open(database.parent_dir+ name, "w+")

        for i in data:
            line = ' '.join(str(x) for x in i)
            f.write(line + '\n')
            
    def readFile (name):
        text = open(database.parent_dir +name)
        file = text.readlines()
        print(file)
        text.close()
        return file

    def createFile (self, song):
        for trackIndex, track in enumerate (song):
            ps.make_wav (
                track,
                bpm = 180,
                transpose = 1,
                pause = 0.0,
                boost = 1.3,
                repeat = 2,
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

# database.createDirectory("one")
# database.createFile("","\one\iets.wav",bach)        
# database.readFile( "\one\iets.wav")
     
