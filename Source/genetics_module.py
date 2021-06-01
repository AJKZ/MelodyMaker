import random

from measure import Measure
from song import Song


def generate_individual_name(index):
    return f'track_{str(1000 + track_index) [1:]}.wav'

def mutate(measure):
    mutatedMeasure = []
    # gives random floating numbers between 0 and 1
    mutateChance = random.random()
    # if chance is between 0.1 and 0.25 we mutate 1 note
    if mutateChance > 0.1 and mutateChance <= 0.25:
        # random a note to mutate 
        mutatedNote1 = random.randrange(0,4)
        mutatedNote2 = random.randrange(0,4)
        while(mutatedNote1 == mutatedNote2):
            mutatedNote2 = random.randrange(0,4)
        print("point mutation",mutatedNote1,mutatedNote2)
        mutatedMeasure = measure
        mutatedMeasure[mutatedNote1] = measure[mutatedNote2]
        #mutatingMeasure[mutatedNote2] = measure[mutatedNote1]
    elif mutateChance > 0.05 and mutateChance <= 0.1:
        shift = random.randrange(1,4)
        print("shift mutation :" , shift)
        for note in range (len(measure)):
            mutatedMeasure.append(measure[(note+shift)% 4])
    elif mutateChance < 0.05:
        print("gen mutation")
        for note in range (len(measure)):
            mutatedMeasure.append(measure[random.randrange(0,4)])
    else:    
        print("measure not mutated")
        mutatedMeasure = measure

    return mutatedMeasure

def generate_initial_population(population_size , measures_amount):
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
