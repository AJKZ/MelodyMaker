import random

from measure import Measure
from song import Song


def generate_individual_name(index):
    return f'track_{str(1000 + track_index) [1:]}.wav'

def mutate(measure):
    mutated_measure = []
    # gives random floating numbers between 0 and 1
    mutate_chance = random.random()
    # if chance is between 0.1 and 0.25 we mutate 1 note
    if mutate_chance > 0.1 and mutate_chance <= 0.25:
        # random a note to mutate 
        mutated_note1 = random.randrange(0,4)
        mutated_note2 = random.randrange(0,4)
        while(mutated_note1 == mutated_note2):
            mutated_note2 = random.randrange(0,4)
        print("point mutation",mutated_note1,mutated_note2)
        mutated_measure = measure
        mutated_measure[mutated_note1] = measure[mutated_note2]
        #mutatingMeasure[mutated_note2] = measure[mutated_note1]
    elif mutate_chance > 0.05 and mutate_chance <= 0.1:
        shift = random.randrange(1,4)
        print("shift mutation :" , shift)
        for note in range (len(measure)):
            mutated_measure.append(measure[(note+shift)% 4])
    elif mutate_chance < 0.05:
        print("gen mutation")
        for note in range (len(measure)):
            mutated_measure.append(measure[random.randrange(0,4)])
    else:    
        print("measure not mutated")
        mutated_measure = measure

    return mutated_measure

def generate_initial_population(population_size , measures_amount ):
    #can make global
    note_list = [('c4', 4), ('d', 4), ('e', 4), ('f', 4),('g', 4), ('a', 4), ('b', 4),('c5',4)]
    #to store list of all measures
    measure_population = []
    #to store list of all songs
    song_population = []

    #for each individual in your population
    for individual in range(population_size) :
        #We create a temporary variable 
        measureNotes = []
        #append a song to song list
        song_population.append(Song())
        #if loop to append notes for a measure
        for note in range ((measures_amount * 4)+1):
            #if modulus 4 and we are not at index 0
            if note % 4 == 0 and note != 0:
                # we append a measure to the measure list
                measure_population.append(Measure())
                #from the last measure we put in the measure list we append the measure we appended (line 63 )
                measure_population[len(measure_population)-1].notes = measureNotes
                #we also append the measure to the last song in we appended in the song list
                song_population[individual].measures.append(measure_population[len(measure_population)-1].notes)
                # we clear the temporary variabel
                measureNotes = []
            # append nodeds to make a measure of 4/4    
            measureNotes.append(note_list[random.randrange(0,len(note_list))])
    #return the song list 
    return song_population
