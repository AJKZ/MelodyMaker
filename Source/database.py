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


    def generate_song(self, generation_num: str, song_name: str, song: list):
        song_name += '.wav'
        for note_index, note in enumerate(song):
            ps.make_wav (
                note,
                bpm = 180,
                transpose = 1,
                pause = 0.0,
                boost = 1.3,
                repeat = 0,
                fn = self.root_path.joinpath(str(generation_num)).joinpath(str(song_name)).as_posix()
            )

        return


    def write_song_to_file(self, generation, song_name, song):
        f = self.root_path.joinpath(str(generation)).joinpath(str(song_name)).open('w+')
        f.write_text('[[')
        for measure in song:
            for note in measure:
                f.write_text(str(note))
                f.write_text(',')
        f.write_text(']]')


    # def get_song_names(self, generation):
    #     search_dir = self.root_path.joinpath(str(generation)).glob('**/*')
    #     song_names = [song for song in search_dir if song.is_file()]
    #     return song_names


    @property
    def root_path(self):
        return self._root_path


    @root_path.setter
    def root_path(self, new_path):
        self._root_path = new_path
