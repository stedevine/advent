"""This script solves the first question on http://adventofcode.com/day/3"""

# Santa is visting houses on an infinite 2-d grid.
# instructions >,<, ^ and v move him right, left, up and down
# He delivers a present at every house (including the one at the start position)
# How many houses receive at least one present?
# (Or - how many unique houses does he visit?)

# When Santa visits a house express the position as a string
# then add this string to a dictionary
# (each item will be unique)

def get_position(position, instruction):
    """Given the current position and the instruction get the new position"""
    if instruction == '>':
        position['x'] += 1
    elif instruction == '<':
        position['x'] -= 1
    elif instruction == '^':
        position['y'] += 1
    elif instruction == 'v':
        position['y'] -= 1

    return position

def get_position_as_string(position):
    """Given a postion return that position as a string"""
    return "x:" + str(position['x']) + ", y:" + str(position['y'])

def number_of_unique_visits(instructions):
    """count the number of unique visits"""

    position = {'x' : 0, 'y' : 0}
    # explicitly visit 0,0
    unique_visits = {get_position_as_string(position)}

    for instruction in instructions:
        position = get_position(position, instruction)
        unique_visits.add(get_position_as_string(position))

    return len(unique_visits)

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read()

print(number_of_unique_visits(read_file('input.txt')))
