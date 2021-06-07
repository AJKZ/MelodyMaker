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
from random import randint

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
    
    population = gn.generate_initial_population(population_size, measures_per_song)

    current_generation = 0
    while current_generation < max_generations:
        db.create_generation_dir(str(current_generation))

        # generate (.wav & .txt), present (listen to), and rate songs
        for song_idx, song in enumerate(population):
            db.generate_song(str(current_generation), str(song_idx), song.write_format())
            song_path = db.root_path.joinpath(str(current_generation)).joinpath(str(song_idx)).as_posix()
            db.write_song_to_file(current_generation, song_path + '.txt', song)
            population[song_idx].fitness_score = gn.fitness(song_path + '.wav')

        # generate children with highest scoring parents
        parents = gn.selection(population)
        next_generation = [
                    gn.crossover_notes(parents) if measures_per_song == 1 
                else gn.crossover_measures(parents)
            for i in range(num_crossovers)
        ]

        # mutate measures (chance randomizer happens in function)
        for song_idx in range(len(population[2:])):
            for measure_idx in range(measures_per_song):
                population[song_idx].measures[measure_idx] = gn.mutate(population[song_idx].measures[measure_idx])
        
        # fill up rest of next generation with random selection out of population not used as parents
        while len(next_generation) < population_size:
            selection_chance = randint(1, population[2].fitness_score)

            for song_idx, song in enumerate(population):
                if song.fitness_score > selection_chance:
                    selected_song = population.pop(song_idx)
                    break

            next_generation.append(selected_song)

        population = next_generation

        current_generation += 1


if __name__ == '__main__':
    main()
