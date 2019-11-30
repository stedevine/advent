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

house_number = 0
total = 0
while (total < 34000000):
    house_number += 1
    total = get_total(house_number)
    print('{} {}'.format(house_number, total))

print(house_number)
