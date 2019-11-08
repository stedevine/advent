from lib import get_replacement_dictionary, get_molecule, get_element_list

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


# Input molecule : HOH
# Transformations
# H -> HO, OH
# O -> HH
if __name__ == '__main__':
    molecule = 'HOAiH'
    replacement_dictionary = {
        'H' : ['HO', 'OH'],
        'O' : ['HH'],
        'Ai': ['R']
    }
    print(generate_molecules(molecule, replacement_dictionary))
    replacement_dictionary = get_replacement_dictionary('./medicine_input.txt')
    molecule = get_molecule('./medicine_input.txt')
    print(len(generate_molecules(molecule, replacement_dictionary)))
