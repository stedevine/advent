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
