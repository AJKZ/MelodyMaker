"""
Melody Maker project
AUTHORS: Alan Zhong, Jarno Biesheuvel, Jozef Chen

Program should emulate a genetic algorithm that
reconstructs music tracks based on user input

NOTE :
OPTIONAL
so that the console isn't flooded with prints:
In `tomita` module,
comment out the prints in `mkfreq.py#getfreq`,
also in `pysynth.py` lines 151, 158, 187
"""

import ast
import click
import os
from pathlib import Path

import genetics as gn
from database import Database
from measure import Measure
from song import Song


@click.command()
@click.option('--population_size', default=10, prompt='Population size, default', type=int)
@click.option('--measures_per_song', default=4, prompt='Measures per song, default', type=int)
@click.option('--max_generations', default=8, prompt='Max generations, default', type=int)
@click.option('--num_crossovers', default=6, prompt='Number of crossovers per generation, default', type=int)
def main(population_size: int, measures_per_song: int, max_generations: int, num_crossovers: int):
    db = Database()
    
    population = gn.generate_initial_population(init_population_size, measures_per_song)

    current_generation = 0
    while current_generation < max_generations:
        db.create_generation_dir(str(current_generation))

        # generate (.wav & .txt), present (listen to), and rate songs
        for song_idx, song in enumerate(population):
            db.generate_song(str(current_generation), str(song_idx), song.write_format())
            song_path = db.root_path.joinpath(str(current_generation)).joinpath(str(song_idx)).as_posix()
            db.write_song_to_file(current_generation, song_path + '.txt', song)
            population[song_idx].fitness_score = gn.fitness(song_path + '.wav', population[song_idx])

        parents = gn.selection(population)

        current_generation += 1


if __name__ == '__main__':
    main()
