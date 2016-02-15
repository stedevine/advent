"""This script solves the first question on http://adventofcode.com/day/1"""

def floor_finder(instructions):
    """To what floor do the instructions send Santa?"""
    # ( -> move up
    # ) -> move down
    return instructions.count('(') - instructions.count(')')

def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read()

print(floor_finder(read_file('input.txt')))
