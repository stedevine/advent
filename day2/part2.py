"""This script solves the second question on http://adventofcode.com/day/2"""

def calculate_ribbon_length(file_name):
    """Get total length of required ribbon for presents"""
    # ribbon required for each present is :
    # perimeter of smallest side + bow length
    # the bow length is equal to the volume
    # (except it is in one dimension)
    total_length = 0
    for present in tuple(open(file_name, 'r')):
        dimensions = present.split('x')
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        perimeter1 = (2 * length) + (2 * width)
        perimeter2 = (2 * width) + (2 * height)
        perimeter3 = (2 * height) + (2 * length)

        ribbon = min(perimeter1, min(perimeter2, perimeter3))
        bow = length * width * height
        total_length += ribbon + bow

    return total_length

print(calculate_ribbon_length('input.txt'))
