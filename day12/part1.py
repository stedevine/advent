import json
from jsonCounter import JsonCounter
from jsonCounter import JsonCounterNoRed

with open("input.json") as json_file:
    data = json.load(json_file)

# part 1 - count all the numbers in the file
print(JsonCounter.getTotalForObject(data))
# part 2 - count all the numbers except those in objects that contain the value "red"
print(JsonCounterNoRed.getTotalForObjectNoRed(data))
