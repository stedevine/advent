
# For a list of routes : a to b = 10
# Where a and b are locations and 10 is the distance
# find the shortest path that visits every location exactly once.
# The list contains distances for *every* pair of locations
# (if we think of this as a graph - every node in the graph is connected to every other node)

# Try a brute force approach  - start at each node then visit the closest node, from that node
# visit the closest unvisited node, repeat until all nodes are visited.

def getDistance(locationA, locationB, locations):
    entry = next((x for x in locations if (x["start"] == locationA and x["end"] == locationB) or (x["end"] == locationA and x["start"] == locationB)), None)
    if entry is None:
        return 0
    return entry["distance"]

def getLocation(line):
    start = line.split(" to ")[0]
    end = line.split(" to ")[1].split(" = ")[0]
    distance = int(line.split(" = ")[1])
    result = { "start" : start, "end" : end, "distance" : distance }
    #print(result)
    return result

locations = []
f = open('input.txt','r')
for line in f:
    locations.append(getLocation(line))

'''
locations = [
{ "start" : "London", "end" : "Dublin", "distance" : 464 },
{ "start" : "London", "end" : "Belfast", "distance" : 518 },
{ "start" : "Dublin", "end" : "Belfast", "distance" : 141 }]
'''

distances = []
toStart = set()
for item in locations :
    toStart.add(item["start"])
    toStart.add(item["end"])

#print(toStart)
for currentLocation in toStart :
    toVisit = list(toStart)
    #print(currentLocation)

    totalDistance = 0
    toVisit.remove(currentLocation)
    totalDistance = 0

    while toVisit:
        # What are the available destinations and their distances
        nextlocations = []
        for destination in toVisit :
            nextlocations.append({"end" : destination, "distance" : getDistance(currentLocation, destination, locations)})

        #print (nextlocations)
        # select the closest one
        closestlocation = min(nextlocations, key=lambda x : x["distance"])
        #print (closestlocation)

        # visit this location
        currentLocation = closestlocation["end"]
        toVisit.remove(currentLocation)
        totalDistance += closestlocation["distance"]

    #print(totalDistance)
    distances.append(totalDistance)

print(min(distances))
