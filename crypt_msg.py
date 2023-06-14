import sys
import os

sys.path.append("/var/lib/python")
from messages.creator import MessageGenerator
os.chdir("/var/local/slackmessages")


def leeting(text):
    leetdict = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '9',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2',
        'A': '@',
        'E': '€',
        'T': '†',
        'I': '1',
        'O': 'Ω',
        'S': '5',
        'F': 'ƒ',
        'Z': '2',
        '0': ')',
        '1': '!',
        '2': '@',
        '3': '#',
        '4': '$',
        '5': '%',
        '6': '^',
        '7': '&',
        '8': '*',
        '9': '('
    }
    leettext = ''
    for char in text:
        leettext += leetdict.get(char, char)
    return leettext


filename1 = 'strings.txt'
filename = 'slackmessages.txt'
with open(filename1, 'r') as file1:
    with open(filename, 'w') as file:
        creator = MessageGenerator(filename1)
        file.write(creator.generate_message())
with open(filename, 'r') as file:
    text = file.read()
    leettext = leeting(text)
print(leettext)
