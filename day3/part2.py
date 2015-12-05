def getNewPosition(character, currentxposition, currentyposition):
    if (character == '>'):
        currentxposition += 1
    elif (character == '<'):
        currentxposition -= 1
    elif (character == '^'):
        currentyposition += 1
    elif (character == 'v'):
        currentyposition -= 1

    return (currentxposition, currentyposition)

def processCharacter(character, currentxposition, currentyposition, numberOfPointsVisitedAtLeastOnce, pointsVisited):
    p = getNewPosition(character, currentxposition, currentyposition)
    currentxposition = p[0]
    currentyposition = p[1]
    pointsVisited.append((currentxposition,currentyposition))
    #print(pointsVisited)
    numberOfTimesPointVisited = len([item for item in pointsVisited if item[0] == currentxposition and item[1] == currentyposition])
    #print(numberOfTimesPointVisited)
    if (1 == numberOfTimesPointVisited):
        numberOfPointsVisitedAtLeastOnce += 1

    #print(numberOfPointsVisitedAtLeastOnce)

    return (numberOfPointsVisitedAtLeastOnce, currentxposition, currentyposition)

f = open('input.txt','r')
data = f.read()
#data = "^^^^^^vv"
pointsVisited = []
santaxpos = 0
santaypos = 0
roboxpos = 0
roboypos = 0

numberOfPointsVisitedAtLeastOnce = 1
pointsVisited.insert(0, (santaxpos,santaypos))

alternate = 0

for character in data:
    if (alternate % 2 == 0):
        #processCharacter(character, santaxpos, santaypos, numberOfPointsVisitedAtLeastOnce, pointsVisited)
        result = processCharacter(character, santaxpos, santaypos, numberOfPointsVisitedAtLeastOnce, pointsVisited)
        numberOfPointsVisitedAtLeastOnce = result[0]
        santaxpos = result[1]
        santaypos = result[2]
        #output = "s {x},{y}".format(x=santaxpos,y=santaxpos)
        #print(output)
    else:
        result = processCharacter(character, roboxpos, roboypos, numberOfPointsVisitedAtLeastOnce, pointsVisited)
        numberOfPointsVisitedAtLeastOnce = result[0]
        roboxpos = result[1]
        roboypos = result[2]
        #output = "r {x},{y}".format(x=roboxpos,y=roboypos)
        #print(output)

    alternate += 1

print(numberOfPointsVisitedAtLeastOnce)
