def hasTwoPairs(line):
    # find index of first pair
    linelength = len(line)
    for i in range (0, linelength -1, 1):
        pair = (line[i], line[i+1])
        for j in range (i+2, linelength -1, 1):
            if (pair[0] == line[j] and pair[1] == line[j+1]):
                output = "{p}{q}".format(p=pair[0], q=pair[1])
                #print(output)
                return True

    return False



def containsPattern(line):
    # Pattern is letter which repeats with exactly one letter separating them
    linelength = len(line)
    for i in range (0, linelength -2, 1):
        if (line[i]==line[i+2]):
            return True

    return False

def isNice(line):
    return hasTwoPairs(line) and containsPattern(line)

# unit tests
print(isNice('qjhvhtzxzqqjkmpb'))
print(isNice('xxyxx'))
print(isNice('uurcxstgmygtbstg'))
print(isNice('ieodomkazucvgmuy'))
f = open('input.txt','r')
count = 0
for line in f:
    if (isNice(line)):
        count += 1

print(count)
