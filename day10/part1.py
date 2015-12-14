# Look say
# 1 -> 11 (one "one")
# 11 -> 21 (two "ones")
# 21 -> 1211 (one "two", one "one")

def getNext(value):
    strValue = str(value)
    output = ""
    index = 0
    while (index < len(strValue)):
        digit = strValue[index]
        digitCount = 1
        index += 1
        while (index < len(strValue) and digit == strValue[index]):
            digitCount += 1
            index += 1
        output += str(digitCount)
        output += str(digit)

    return output
    # count the number of identical digits


input = 1113122113
for i in range(40):
    #print (input)
    input = getNext(input)

print("{i} iterations length={l}".format(i=40,l=len(input)))

for i in range(10):
    #print (input)
    input = getNext(input)

print("{i} iterations length={l}".format(i=50,l=len(input)))
