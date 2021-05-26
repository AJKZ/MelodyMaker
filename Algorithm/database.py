import glob as gl
import os
import shutil
import tomita.legacy.pysynth as ps
# import tomita.legacy.pysynth as ps
# path in methods should be treated that, folder of python file is home folder 

class database:

    m_bpm = 180,
    m_transpose = 1,
    m_pause = 0.0,
    m_boost = 1.3,
    m_repeat = 2,

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
        print(database.parent_dir +name)
        text = open(database.parent_dir +name)
        
        file = text.readlines()
        print(file)
        text.close()
        return file

    def createFile (self, song):
        for trackIndex, track in enumerate (song):
            ps.make_wav (
                track,
                bpm = database.m_bpm,
                transpose = database.m_transpose,
                pause = database.m_pause,
                boost = database.m_boost,
                repeat = database.m_repeat,
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
database.readFile( "\BuildingBlocks\Bach.py")
     
