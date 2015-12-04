# total ribbon length
# smallest perimeter (ribbon) + volume (bow)
f = open('input.txt','r')
totallength = 0
for line in f:
    dimensions = line.split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    perimeter1 = (2 * length) + (2 * width)
    perimeter2 = (2 * width) + (2 * height)
    perimeter3 = (2 * height) + (2 * length)

    ribbon = min(perimeter1, min(perimeter2, perimeter3))
    bow = length * width * height
    totallength += ribbon + bow

print(totallength)
