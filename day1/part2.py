# At which instruction does Santa first enter the basement
# that is the current floor = -1
# The first instruction is 1 (not 0)
# ( -> move up
# ) -> move down

f = open('input.txt','r')
data = f.read()
currentFloor = 0
index = 1
for character in data:
    if (character == '('):
        currentFloor += 1
    else:
        currentFloor -= 1

    if (currentFloor == -1):
        print(index)
        break

    index += 1
