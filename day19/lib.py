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

# Break down a molecule string to a list of elements
# e.g. AiHOrKNe -> ['Ai', 'H', 'Or', 'K', 'Ne']
def get_element_list(input_molecule):
    # element start with an uppercase letter
    # Get the indices of all the uppercase letters
    indices_of_elements = [i for i, e in enumerate(input_molecule)
    if e.isupper()] + [len(input_molecule)]

    # Iterate over the list of indices and a second list of indices offset by 1
    # This gives us the indices of the start and end of each element
    # Use the string's substring method to add each element from the molecule to a list
    return [input_molecule[x:y] for x, y in zip(indices_of_elements, indices_of_elements[1:])]
