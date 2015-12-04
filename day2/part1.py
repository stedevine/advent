f = open('input.txt','r')
totalarea = 0
for line in f:
    dimensions = line.split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    a = (int)(length * width)
    b = width * height
    c = height * length
    slack = min(a, min(b, c))
    totalarea = totalarea + (2 * a) + (2 * b) + (2 * c) + slack
print(totalarea)
