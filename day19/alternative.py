from lib import get_replacement_dictionary, get_molecule, get_reversed_dictionary
import re
from random import shuffle
from queue import PriorityQueue

def expand_iter(input, transitions):
    for src in transitions:
        for dst in transitions[src]:
            for match in re.finditer(src, input):
                yield input[:match.start()] + dst + input[match.end():]


# Input molecule : HOH
# Transformations
# H -> HO, OH
# O -> HH
if __name__ == '__main__':
    molecule = 'HOAiH'
    # key : element
    # value : list of elements which can be substituted for key
    replacement_dictionary = {
        'H' : ['HO', 'OH'],
        'O' : ['HH'],
        'Ai': ['R']
    }
    expansions = set(expand_iter(molecule, replacement_dictionary))
    print(len(expansions))

    replacement_dictionary = get_replacement_dictionary('./medicine_input.txt')
    molecule = get_molecule('./medicine_input.txt')
    expansions = set(expand_iter(molecule, replacement_dictionary))
    print(len(expansions))

    reversed_dictionary = get_reversed_dictionary('./medicine_input.txt')
    #q = PriorityQueue()
    #q.put((len(molecule), 0, molecule))
    q = set()
    q.add((len(molecule),0,molecule))
    while True:
        q = list(q)
        shuffle(q)
        length, iterations, current = q[0]
        print('{} {}'.format(iterations,current))
        if current == 'e':
            break

        for precursor in expand_iter(current, reversed_dictionary):
            q.append((len(precursor), iterations + 1, precursor))

    print(iterations)
