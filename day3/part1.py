f = open('input.txt','r')
data = f.read()
pointsVisited = {}
xpos = 0
ypos = 0

visitedatleastonce = 1
pointsVisited[hash((xpos, ypos))] = 1
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

    count = pointsVisited.get(hash((xpos, ypos)), 0)  + 1
    pointsVisited[hash((xpos, ypos))] = count
    if (count == 1):
        visitedatleastonce += 1

    output = "{x},{y} {c}".format(x=xpos,y=ypos, c=count, h=hash((xpos, ypos)))
    print(output)

print(visitedatleastonce)
