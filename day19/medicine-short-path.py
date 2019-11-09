from lib import get_molecule

def get_reversed_dictionary(input_file):
    reversed_dictionary = {}
    with open(input_file) as file:
        for line in file:
            if ' => ' in line:
                source = line.split(' => ')[0].strip()
                target = line.split(' => ')[1].strip()
                reversed_dictionary.update({target:source})
    print(reversed_dictionary)
    return reversed_dictionary

def get_step_count(input_molecule, reversed_dictionary):
    # Find the longest chain of elements in the molecule that can be produced from a transformation
    keys = sorted(reversed_dictionary.keys(), key=len)
    keys.reverse()
    steps = 0
    print(input_molecule)
    while(input_molecule != 'e'):
        for key in keys:
            # Is the transformed element in the molecule?
            #print(molecule.find(key))
            index_of_transformed = input_molecule.find(key)
            if index_of_transformed > -1:
                # replace the key with the value
                print('found {} replacing with {}'.format(key, reversed_dictionary[key]))
                steps = steps + 1
                input_molecule = input_molecule.replace(key, reversed_dictionary[key],1)
                print(input_molecule)
                break

    print(input_molecule)
    return steps

def length_of_path_to_e(reversed_dictionary):
    processed_dictionary = {}
    for key in reversed_dictionary.keys():
        steps_to_e = 0
        value = key
        while(True):
            steps_to_e = steps_to_e + 1
            value = reversed_dictionary.get(value)
            if (value == None):
                processed_dictionary.update({key:-1})
                break
            if (value == 'e'):
                processed_dictionary.update({key:steps_to_e})
                break
    print(processed_dictionary)

    #value = reversed_dictionary[key]
    #if value == 'e':
    #    return steps_to_e
    #else:
    #    steps_to_e = steps_to_e + 1
    #    value = reversed_dictionary[value]

    #if value == 'e':
    #    return steps_to_e
    #else:
    #    steps_to_e = steps_to_e + 1
    #    value = reversed_dictionary[value]


def get_count_recursive(input_molecule, reversed_dictionary, step_count):
    print('{} {}'.format(step_count, input_molecule))
    if (input_molecule.strip() == 'e'):
        print('found path')
        return step_count

    keys = sorted(reversed_dictionary.keys(), key=len)
    keys.reverse()
    if any (k in keys for k in input_molecule):
        step_count = step_count + 1
        for key in keys:
            index_of_transformed = input_molecule.find(key)
            if index_of_transformed > -1:
                # replace the key with the value
                #print('found {} replacing with {}'.format(key, reversed_dictionary[key]))
                input_molecule = input_molecule.replace(key, reversed_dictionary[key],1)

    return get_count_recursive(input_molecule, reversed_dictionary, step_count)

    #print('Dead end')
    #return

# e => H
# e => O
# H => HO
# H => OH
# O => HH

# HOH       3 steps
# HOHOHO    6 steps
if __name__ == '__main__':
    molecule = 'HOHOHO'
    reversed_dictionary = {
    'H': 'e',
    'O': 'e',
    'HO': 'H',
    'OH': 'H',
    'HH': 'O'
    }
    print(length_of_path_to_e(reversed_dictionary))

    #print(get_count_recursive(molecule, reversed_dictionary,0))
    # Simple deadend
    molecule = 'KAiHOHOHO'
    reversed_dictionary = {
        'KAiHO' : 'K',
        'HO' : 'H',
        'KAi' : 'H',
        'HH' : 'H',
        'H' : 'e',
        'ee' : 'e'
    }
    print(length_of_path_to_e(reversed_dictionary))
    print(length_of_path_to_e(get_reversed_dictionary('./medicine_input.txt')))
    #print(get_count_recursive(molecule, reversed_dictionary,0))
    #print(get_step_count(get_molecule('./medicine_input.txt'),get_reversed_dictionary('./medicine_input.txt')))
    # NRnBSiRnCaRnFArYFArFArF
    # Need to come up with a new method
