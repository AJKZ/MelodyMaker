import click
import re
from operator import attrgetter
from playsound import playsound
from random import random, randrange, randint

from measure import Measure
from song import Song


NOTES_POOL = [
        ('c', 4), ('d', 4), ('e', 4), ('f', 4), ('g', 4), ('a', 4), ('b', 4), ('c5', 4)
    ]


def generate_individual_name(index):
    return f'track_{str(1000 + index) [1:]}.wav'


def fitness(song_file_name):
    print('\nPlaying song ' + song_file_name.split('generations/')[-1] + '...')
    playsound(song_file_name)
    score = click.prompt('Score (1-10)', type=int)
    return score


def selection(population):
    population.sort(key=lambda song: song.fitness_score, reverse=True)
    return [population[0], population[1]]


def crossover_notes(parents):
    child = Song()
    child.measures = [Measure()]

    measure_a, measure_b = parents[0].measures[0], parents[1].measures[0]
    split = randint(1, len(measure_a.notes) - 1)
    child.measures[0].notes += measure_a.notes[0:split] + measure_b.notes[split:]

    return child


def crossover_measures(parents):
    child = Song()

    measures_a, measures_b = parents[0].measures, parents[1].measures
    split = randint(1, len(measures_a) - 1)
    child.measures += measures_a[0:split] + measures_b[split:]

    return child


def mutate(measure):
    mutate_chance = random()
    mutated_measure = Measure()

    if mutate_chance > 0.2 and mutate_chance <= 0.35:
        print('\nA measure undergoes point mutation\nOld measure: ', measure.string_format())
        mutated_note1 = randrange(0, 4)
        mutated_note2 = randrange(0, 4)

        while(mutated_note1 == mutated_note2):
            mutated_note2 = randrange(0, 4)
        
        mutated_measure = measure
        mutated_measure.notes[mutated_note1] = measure.notes[mutated_note2]
        print('Mutated measure: ', mutated_measure.string_format())

    elif mutate_chance > 0.15 and mutate_chance <= 0.2:
        print('\nA measure undergoes shift mutation\nOld measure: ', measure.string_format())
        shift = randrange(1, 4)

        for note in range (len(measure.notes)):
            mutated_measure.notes.append(measure.notes[(note + shift) % 4])
        print('Mutated measure: ', mutated_measure.string_format())

    elif mutate_chance <= 0.15:
        print('\nA measure undergoes gene mutation\nOld measure: ', measure.string_format())
        for note in range (len(measure.notes)):
            mutated_measure.notes.append(measure.notes[randrange(0, 4)])
        print('Mutated measure: ', mutated_measure.string_format())

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

            measure_notes.append(NOTES_POOL[randrange(0, len(NOTES_POOL))])

    return song_population
