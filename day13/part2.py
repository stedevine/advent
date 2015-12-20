# Given a list of people and the happiness/unhappiness they feel when sitting next to
# any of the other people in the list, figure out the optimal arrangement when seating them
# around a circular table.

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

# map the first letter of each peron's name into their points relationship
def get_relationship(line):
    words = line.split(" ")
    points = int(words[3])
    if (words[2] == "lose"):
        points = points * -1
    return {'left': words[0][0], 'right' : words[-1].strip('.\n')[0], 'points': points}

# list comprehension to get the points
# extra conditon if people sit next to you (X) score is 0
def get_points(a, b, relationships):
    if (a == 'X' or b == 'X'):
        return 0

    points = 0
    atob = next((x for x in relationships if x["left"] == a and x["right"] == b), None)
#    print (atob)
    if atob is not None:
        points += atob["points"]

    btoa = next((x for x in relationships if x["left"] == b and x["right"] == a), None)
#    print (btoa)
    if btoa is not None:
        points += btoa["points"]

    return points


relationships = list()
f = open('input.txt','r')
for line in f:
    relationships.append(get_relationship(line))


perms = list(all_perms("ABCDEFGMX"))

pointsList = []
for perm in perms:
    points=0
    for i in range(0, len(perm)-1):
        points += get_points(perm[i],perm[i+1], relationships)
    points += get_points(perm[len(perm)-1],perm[0], relationships)
    #print(points)
    pointsList.append(points)

print(max(pointsList))
