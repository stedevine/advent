# For a 1000 x 1000 grid of lights (which are initially off)
# process a list of instructions that will
# turn on, turn off or toggle a rectangular range of lights
# example: toggle 461,550 through 564,900
# return the final count of lights that are on
from lightGrid import LightGrid

matrix = [[0 for x in range (1000)] for x in range(1000)]
f = open('input.txt','r')
for line in f:
    LightGrid.processInstruction(line,matrix)

print(LightGrid.countOnLights(matrix))
