# Get total length of required ribbon for same presents as part1
# ribbon required for each present is perimeter of smallest side + bow length
# the bow length is equal to the volume (except its in one dimension)
f = open('input.txt','r')
totalLength = 0
for line in f:
    # get dimensions from file
    dimensions = line.split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    perimeter1 = (2 * length) + (2 * width)
    perimeter2 = (2 * width) + (2 * height)
    perimeter3 = (2 * height) + (2 * length)

    ribbon = min(perimeter1, min(perimeter2, perimeter3))
    bow = length * width * height
    totalLength += ribbon + bow

print(totalLength)
