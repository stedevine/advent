# For a 1000 x 1000 grid of lights (which are initially off)
# process a list of instructions that will
# increase or decrease the brightness level of a rectangular range of lights
# example: toggle 461,550 through 564,900 : set brightness level of range by 2
# note: decrease goes to a minimum value of 0, no negative values.
# return the final count of lights that are on
from brightGrid import BrightGrid

matrix = [[0 for x in range (1000)] for x in range(1000)]
f = open('input.txt','r')
for line in f:
    BrightGrid.processInstruction(line,matrix)

print(BrightGrid.countTotalBrightness(matrix))
