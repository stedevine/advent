# How many different combinations of containers can exactly fit all 150 liters of eggnog?
# There are 20 different containers.
# 11111111111111111111 (base2) --> 1048575 (base 10
# there are 1048575 different possible combinations of these containers

count = 0
con = [33,14,18,20,45,35,16,35,1,13,18,13,50,44,48,6,24,41,30,42]
#con=[20, 15, 10, 5, 5]
print(len(con))
for i in range(1, 1048575):
    combination = list(bin(i))
    # drop the leading '0b'
    combination.pop(0)
    combination.pop(0)
    # add the leading zeros to the list
    while (len(combination) < len(con)):
        combination =  ['0'] + combination

    #print (combination)

    total = 0
    for c in range(0, len(combination)):
        if (combination[c] == '1'):
            total += con[c]

    if total == 150:
        print(combination)
        print(total)
        count += 1
print(count)
    #print(list(bin(i).strip("0b")))
    #on_bits = [sues.index(s) for s in sues if (item_name in s)



#print(bin(127).strip("0b"))
#print(list(bin(157).strip("0b")))
