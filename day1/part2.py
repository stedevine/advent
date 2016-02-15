"""This script solves the second question on http://adventofcode.com/day/1"""

def basement_position(instructions):
    """At which instruction does Santa first enter the basement?"""
    # The basement is level -1
    # The position of the first instruction is 1 (not 0)
    # ( -> move up
    # ) -> move down
    # Other characters are not supported.

    current_floor = 0
    position = 1
    for instruction in instructions:
        if instruction == '(':
            current_floor += 1
        else:
            current_floor -= 1

        if current_floor == -1:
            return position

        position += 1

    # not found
    return -1

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read()

print(basement_position(read_file('input.txt')))
