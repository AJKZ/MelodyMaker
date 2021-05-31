"""
Melody Maker project
AUTHORS: Alan Zhong, Jarno Biesheuvel, Jozef Chen
"""

from note import Note
from measure import Measure
from song import Song
import ast


def main():
    note1 = Note('a', 4)
    note2 = Note.with_tuple(('b', 4))

    print(note1.pitch)
    print(note2.pitch)
    # note3 = Note('c', 4)
    # note4 = Note('d', 4)
    
    # measure1 = Measure()
    # measure1.notes = [note1, note2]
    # measure2 = Measure()
    # measure2.notes = [note3, note4]

    # song = Song()
    # song.measures = [measure1, measure2]

    # f = open('Test.txt', 'w+')
    # f.write(song.format_string())
    # f.close()

    # with open('Test.txt') as s:
    #     a = ast.literal_eval(s.read())

    # print(a)


if __name__ == '__main__':
    main()
