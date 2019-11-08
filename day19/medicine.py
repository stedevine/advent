# Input molecule : HOH
# Transformations
# H -> HO, OH
# O -> HH

def get_replacement_dictionary(input_file):
    replacements = {}
    with open(input_file) as file:
        for line in file:
            if ' => ' in line:
                key = line.split(' => ')[0].strip()
                value = line.split(' => ')[1].strip()
                if key not in replacements:
                    replacements.update({key:[value]})
                else:
                    replacements[key].append(value)

    return replacements

def get_molecule(input_file):
    with open(input_file) as file:
        # molecule is the last line in the input file
        return list(file)[-1].strip()

def generate_molecules(input_molecule, replacement_dictionary):
    # Turn the input string into a list of elements.
    element_list = get_element_list(input_molecule)
    unique_molecules = set()
    for i in range(0,len(element_list)):
        # We can only change the element if there is a replacement defined for
        # the specific molecule
        if replacement_dictionary.get(element_list[i]):
            # Only apply the replacement to a single element
            # Leave the rest of the molecule unchanged.
            first_part = ''.join(element_list[0:i])
            second_part = ''.join(element_list[i+1:len(element_list)])
            for replacement in replacement_dictionary.get(element_list[i]):
                transformed_molecule = '{}{}{}'.format(first_part, replacement, second_part)
                unique_molecules.add(transformed_molecule)

    return unique_molecules

def get_element_list(input_molecule):
    # element start with an uppercase letter
    # Get the indices of all the uppercase letters
    indices_of_elements = [i for i, e in enumerate(input_molecule)
    if e.isupper()] + [len(input_molecule)]

    # Iterate over the list of indices and a second list of indices offset by 1
    # This gives us the indices of the start and end of each element
    # Use the string's substring method to add each element from the molecule to a list
    return [input_molecule[x:y] for x, y in zip(indices_of_elements, indices_of_elements[1:])]

if __name__ == '__main__':
    molecule = 'HOAiH'
    replacement_dictionary = {
        'H' : ['HO', 'OH'],
        'O' : ['HH'],
        'Ai': ['R']
    }
    print(generate_molecules(molecule, replacement_dictionary))
    #print(len(generate_molecules(molecule, replacement_dictionary)))
    replacement_dictionary = get_replacement_dictionary('./medicine_input.txt')
    molecule = get_molecule('./medicine_input.txt')
    print(len(generate_molecules(molecule, replacement_dictionary)))
