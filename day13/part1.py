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

#def happiness_between_two_people(person1, person2, map):

def get_relationship(line):
    words = line.split(" ")
    points = int(words[3])
    if (words[4] == "lose"):
        points = points * -1
    return {'left': words[0], 'right' : words[-1].trim('.'), 'points': points}
#print("\n".join(all_perms("ABDC")))

relationships = list()
f = open('input.txt','r')
for line in f:
    relationships.append(get_relationship(line))

print(relationships)
