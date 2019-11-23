def presents_at_house(house_number):
    total_presents = 0
    for elf in range(1, house_number + 1):
        #print('{} % {} {}'.format(house_number, elf, house_number % elf == 0))
        if (house_number % elf == 0):
            total_presents = total_presents + int(house_number / elf)

    return total_presents * 10

puzzle_input = 34000000
house_number = 0

# Use binary search
min = 0
max = 500000000

while(True):
    current_value = presents_at_house(house_number)
    print('{}={}'.format(house_number, current_value))
    if (current_value > puzzle_input):
        max = house_number - 1
    elif (current_value < puzzle_input):
        min = house_number + 1
    house_number = int((min + max) / 2)

'''
while (current_value < puzzle_input):
    house_number = house_number + 1
    print(house_number)
    current_value = presents_at_house(house_number)

print(house_number)
'''
