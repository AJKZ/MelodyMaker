"""
Melody Maker project
AUTHORS: Alan Zhong, Jarno Biesheuvel, Jozef Chen

Program should emulate a genetic algorithm that
reconstructs music tracks based on user input

NOTE :
OPTIONAL
In `tomita` module, comment out the prints in `mkfreq.py#getfreq`,
so that the console isn't flooded with piano key information
"""

import ast
import os
from pathlib import Path
from playsound import playsound

import genetics_module as gn
from database import Database
from measure import Measure
from song import Song


def main():
    db = Database()

    db.create_generation_dir('one')
    
    path_to_bach = Path(os.getcwd()).parent.joinpath('sample_song.txt').as_posix()
    with open(path_to_bach) as b:
        bach = ast.literal_eval(b.read())

    bach = [bach[0] + bach[1]]
    i = 1
    db.generate_song('one', str(i), bach)

    # path = Path(os.getcwd()).parent.joinpath('song.wav').as_posix()
    # playsound(path)


if __name__ == '__main__':
    main()
