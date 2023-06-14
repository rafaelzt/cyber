import sys
import os

sys.path.append("/var/lib/python")
from messages.creator import MessageGenerator
os.chdir("/var/local/slackmessages")


def leeting(text):
    leetdict = {
        '4' : 'a',
        '8' : 'b',
        '3' : 'e',
        '9' : 'g',
        '1' : 'i',
        '0' : 'o',
        '5' : 's',
        '7' : 't',
        '2' : 'z',
        '@' : 'A',
        '€' : 'E',
        '†' : 'T',
        '1' : 'I',
        'Ω' : 'O',
        '5' : 'S',
        'ƒ' : 'F',
        '2' : 'Z',
        ')' : '0',
        '!' : '1',
        '@' : '2',
        '#' : '3',
        '$' : '4',
        '%' : '5',
        '^' : '6',
        '&' : '7',
        '*' : '8',
        '(' : '9'
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
