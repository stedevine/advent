
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



locations = [
{ "start" : "London", "end" : "Dublin", "distance" : 464 },
{ "start" : "London", "end" : "Belfast", "distance" : 518 },
{ "start" : "Dublin", "end" : "Belfast", "distance" : 141 }]

toStart = [ "London", "Belfast", "Dublin"]
for currentLocation in toStart :
    toVisit = [ "London", "Belfast", "Dublin"]

    totalDistance = 0
    #print(locations)
    # Start at London
    #currentLocation = "London"
    toVisit.remove(currentLocation)
    totalDistance = 0

    while toVisit:
        # What are the available destinations and their distances
        nextlocations = []
        for destination in toVisit :
            nextlocations.append({"end" : destination, "distance" : getDistance(currentLocation, destination, locations)})

        print (nextlocations)
        # select the closest one
        closestlocation = min(nextlocations, key=lambda x : x["distance"])
        print (closestlocation)

        # visit this location
        currentLocation = closestlocation["end"]
        toVisit.remove(currentLocation)
        totalDistance += closestlocation["distance"]

    print(totalDistance)
