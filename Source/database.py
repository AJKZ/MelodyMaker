"""
Database class
Creates a folder where the populations are stored
Will create a folder for each generation
Is able to read and write songs
"""

import ast
import glob as gl
import os
import shutil
from pathlib import Path

import tomita.legacy.pysynth as ps


class Database:
    def __init__(self):
        self.root_path = Path(os.getcwd()).parent.absolute().joinpath('generations')
        
        if os.path.exists(self.root_path):
            shutil.rmtree(self.root_path)
        
        self.root_path.mkdir()

    def create_generation_dir(self, generation_num):
        self.root_path.joinpath(str(generation_num)).mkdir()

    def generate_song(self, path, data, name):
        if '.wav' in path:
            for track_index, track in enumerate(data):
                ps.make_wav (
                    track,
                    bpm = 180,
                    transpose = 1,
                    pause = 0.0,
                    boost = 1.3,
                    repeat = 1,
                    fn = self.get_track_file_name(track_index),
                )
            
            ps.mix_files (
                *[self.get_track_file_name(track_index) for track_index in range(len(data))],
                self.root_path.joinpath('generation').as_posix()
            )
            
            for file_name in gl.glob('track_*.wav'):
                os.remove(file_name)
            return
        try:
            os.remove(self.root_path.joinpath('generation'))
        except OSError:
            print('Removing old file, and creating new one')

        f = self.root_path.joinpath('generation' + path).open('w+')
        f.write_text('[')
        for bar in data:
            f.write_text('[')
            for note in bar:
                f.write_text(str(note))
                f.write_text(',')
            f.write_text('],')
        f.write_text(']')

    def get_songs(self, name):
        """
        Reads into a generation's directory,
        parses the songs into Song and Measure objects,
        and returns a list of the Song objects
        """
        with open(database.parent_dir + name) as f:
            file = ast.literal_eval(f.read())

        return file

    def get_track_file_name(self, track_index):  
        return f'track_{str(1000 + track_index) [1:]}.wav'

    @property
    def root_path(self):
        return self._root_path

    @root_path.setter
    def root_path(self, new_path):
        self._root_path = new_path
