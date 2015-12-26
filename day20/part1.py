
def countPresents(houseNumber):
    total = 0
    elf = 1
    while houseNumber >= elf :
        if (houseNumber % elf == 0):
            total = total + (elf * 10)
        elf += 1

    return total

houseNumber = 373892
#houseNumber = 500000
#houseNumber = 1000000
presentCount = 0
while presentCount < 34000000:
    houseNumber += 1
    presentCount = countPresents(houseNumber)
    if (houseNumber % 1000 == 0):
        print("{h} {p}".format(h=houseNumber, p=presentCount))


print(houseNumber)
'''
n = 2900
house = [0] * n
for i in range(1,n):
    for j  in range(i,n):
        if (i % j == 0):
            house[j] += i * 10

print (house[4])
'''
