import click
import random
import re
from operator import attrgetter
from playsound import playsound

from measure import Measure
from song import Song


NOTES_POOL = [
        ('c4', 4), ('d', 4), ('e', 4), ('f', 4), ('g', 4), ('a', 4), ('b', 4), ('c5',4)
    ]


def generate_individual_name(index):
    return f'track_{str(1000 + index) [1:]}.wav'


def fitness(song_file_name):
    print('\nPlaying song ' + song_file_name.split('generations/')[-1] + '...')
    playsound(song_file_name)
    score = click.prompt('Score (1-10)', type=int)
    return score


def selection(population):
    sorted_population = sorted(population, key=lambda song: song.fitness_score, reverse=True)
    return (sorted_population[0], sorted_population[1])

def mutate(measure):
    mutated_measure = []
    mutate_chance = random.random()

    if mutate_chance > 0.1 and mutate_chance <= 0.25:
        print('A measure undergoes point mutation')
        mutated_note1 = random.randrange(0, 4)
        mutated_note2 = random.randrange(0, 4)

        while(mutated_note1 == mutated_note2):
            mutated_note2 = random.randrange(0, 4)
        
        mutated_measure = measure
        mutated_measure[mutated_note1] = measure[mutated_note2]

    elif mutate_chance > 0.05 and mutate_chance <= 0.1:
        print("A measure undergoes shift mutation")
        shift = random.randrange(1, 4)

        for note in range (len(measure)):
            mutated_measure.append(measure[(note + shift) % 4])
    elif mutate_chance <= 0.05:
        print("A measure undergoes gene mutation")
        for note in range (len(measure)):
            mutated_measure.append(measure[random.randrange(0, 4)])
    else:
        mutated_measure = measure

    return mutated_measure


def generate_initial_population(song_population_size, measures_per_song):
    measure_population = []
    song_population = []

    for individual in range(song_population_size) : 
        measure_notes = []
        song_population.append(Song())

        measure_position = 0
        for note in range((measures_per_song * 4) + 1):
            if note % 4 == 0 and note != 0:
                measure_population.append(Measure())
                # set notes and position of measure
                measure_population[len(measure_population) - 1].notes = measure_notes
                measure_population[len(measure_population)-1].position = measure_position
                # append measure to measures in song
                song_population[individual].measures.append(measure_population[len(measure_population) - 1])
                measure_notes = []
                measure_position += 1

            measure_notes.append(NOTES_POOL[random.randrange(0, len(NOTES_POOL))])

    return song_population
