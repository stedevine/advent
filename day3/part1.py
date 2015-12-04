f = open('input.txt','r')
data = f.read()
pointsVisited = []
xpos = 0
ypos = 0

# explicitly visit 0,0
numberOfPointsVisitedAtLeastOnce = 1
pointsVisited.insert(0, (xpos,ypos))
output = "{x},{y} {c}".format(x=xpos,y=ypos, c=1)
print(output)

for character in data:
    if (character == '>'):
        xpos += 1
    elif (character == '<'):
        xpos -= 1
    elif (character == '^'):
        ypos += 1
    elif (character == 'v'):
        ypos -= 1

    # how many times have we been here before?
    numberOfTimesPointVisited = len([item for item in pointsVisited if item[0] == xpos and item[1] == ypos])
    if (0 == numberOfTimesPointVisited):
        numberOfPointsVisitedAtLeastOnce += 1

    pointsVisited.append((xpos,ypos))

    output = "{x},{y} {c}".format(x=xpos,y=ypos, c=numberOfTimesPointVisited+1)
    print(output)

print(numberOfPointsVisitedAtLeastOnce)
