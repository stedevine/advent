"""This script solves the first question on http://adventofcode.com/day/2"""

def calculate_total_area(file_name):
    """Calculate the total area of required wrapping paper"""
    # Input is present dimensions: lxwxh
    # Presents are perfect rectangular prisms
    # Required area per present = surface area of present + extra
    # Extra = area of the smallest side
    total_area = 0
    for present in tuple(open(file_name, 'r')):
        dimensions = present.split('x')
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        # get areas of each of the three different faces
        face_a = length * width
        face_b = width * height
        face_c = height * length

        extra = min(face_a, min(face_b, face_c))
        present_area = (2 * face_a) + (2 * face_b) + (2 * face_c) + extra
        total_area = total_area + present_area

    return total_area

print(calculate_total_area('input.txt'))
