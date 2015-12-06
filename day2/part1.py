# Calculate the total area of required wrapping paper
# Input is present dimensions: lxwxh (presents are perfect rectangular prisms)
# Required area per present = surface area of present + extra
# Extra = area of the smallest side
f = open('input.txt','r')
totalArea = 0
for line in f:
    # get dimensions from line
    dimensions = line.split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    # get areas of each of the three different sides
    a = length * width
    b = width * height
    c = height * length
    extra = min(a, min(b, c))
    totalArea = totalArea + (2 * a) + (2 * b) + (2 * c) + extra
print(totalArea)
