import random

from measure import Measure
from song import Song

NOTES_POOL = [
        ('c4', 4),
        ('d', 4),
        ('e', 4),
        ('f', 4),
        ('g', 4),
        ('a', 4),
        ('b', 4),
        ('c5',4)
    ]

def generate_individual_name(index):
    return f'track_{str(1000 + index) [1:]}.wav'

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

        for note in range((measures_per_song * 4) + 1):
            if note % 4 == 0 and note != 0:
                measure_population.append(Measure())
                #from the last measure we put in the measure list we append the measure we appended (line 63 )
                measure_population[len(measure_population) - 1].notes = measure_notes
                #we also append the measure to the last song in we appended in the song list
                song_population[individual].measures.append(measure_population[len(measure_population) - 1])
                measure_notes = []

            measure_notes.append(NOTES_POOL[random.randrange(0, len(NOTES_POOL))])

    return song_population
