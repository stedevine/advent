# Santa is visting houses on an infinite 2-d grid.
# instructions >,<, ^ and v move him right, left, up and down
# He delivers a present at every house (including the one at the start position)
# How many houses receive at least one present?
# (Or - how many unique houses does he visit?)

# Express each house as a 2d point (x,y)
# These points will be stored in a list
# Before appending the point to the list - count the number of times it already exists in the list
# If we've never seen it before, increment the count of unique visits

# explicitly visit 0,0
xpos = 0
ypos = 0
housesVisited = []
housesVisited.insert(0, (xpos,ypos))
uniqueVisits = 1

f = open('input.txt','r')
data = f.read()
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
    # Have we visited this house before?
    if (0 == len([item for item in housesVisited if item[0] == xpos and item[1] == ypos])):
        # no, increment the counter
        uniqueVisits += 1

    housesVisited.append((xpos,ypos))

print(uniqueVisits)
