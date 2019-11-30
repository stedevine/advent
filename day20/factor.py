import math

def get_factors(house_number):
    factors = set()
    limit = int(math.sqrt(house_number))
    #print('input {} limit {}'.format(house_number, limit))
    for i in range(1, limit+1):
        if (house_number % i == 0):
            factors.add(i)
            factors.add(house_number / i)

    return factors

def get_total(house_number):
    factors = get_factors(house_number)
    #print(factors)
    sum = 0
    for factor in factors:
        sum += (house_number) / factor

    return (sum*10)

def get_total_2(house_number):
    factors = get_factors(house_number)
    #print(factors)
    sum = 0
    for factor in factors:
        if (house_number / factor <= 50):
            #print('usable factor {} - total visits {}'.format(factor, house_number / factor))
            sum += factor * 11

    return (sum)

def part_one(puzzle_input):
    # what's the lowest house number to get at least as many presents as the puzzle input
    house_number = 0
    total = 0
    while (total < puzzle_input):
        house_number += 1
        total = get_total(house_number)
        print('{} {}'.format(house_number, total))

    print(house_number)

#part_one(34000000)

# part 2
# Each elf delivers 11 presents (rather than 10) but will only deliver presents to 50 houses
# Elf 1 delivers to houses 1 -> 50, Elf 2 (even numbered houses) 2 -> 100
def part_two(puzzle_input):
    # what's the lowest house number to get at least as many presents as the puzzle input
    house_number = 0
    total = 0
    while (total < puzzle_input):
        house_number += 1
        total = get_total_2(house_number)
        print('{} {}'.format(house_number, total))

    print(house_number)

part_two(34000000)
