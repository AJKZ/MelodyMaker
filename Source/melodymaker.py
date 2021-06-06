"""
Melody Maker project
AUTHORS: Alan Zhong, Jarno Biesheuvel, Jozef Chen

Program should emulate a genetic algorithm that
reconstructs music tracks based on user input

NOTE :
OPTIONAL
In `tomita` module, comment out the prints in `mkfreq.py#getfreq`,
so that the console isn't flooded with piano key information at the start of every run
"""

import ast
import click
import os
from pathlib import Path
from playsound import playsound

import genetics_module as gn
from database import Database
from measure import Measure
from song import Song


@click.command()
@click.option('--init_population_size', default=10, prompt='Initial population size: ', type=int)
@click.option('--measures_per_song', default=4, prompt='Measures per song: ', type=int)
@click.option('--max_generations', default=8, prompt='Max generations: ', type=int)
def main(init_population_size: int, measures_per_song: int, max_generations: int):
    db = Database()
    
    initial_population = gn.generate_initial_population(init_population_size, measures_per_song)

    current_generation = 0
    while current_generation < max_generations:
        db.create_generation_dir(str(current_generation))

        for idx_for_name, song in enumerate(initial_population):
            db.generate_song(str(current_generation), str(idx_for_name), song.write_format())

        current_generation += 1


if __name__ == '__main__':
    main()
