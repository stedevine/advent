def hasThreeVowels(line):
    vowelcount = 0
    for c in line:
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
            vowelcount += 1
        if (vowelcount == 3):
            return True
    return False

def hasDoubleLetter(line):
        for i in range (0, len(line) -1, 1):
            if (line[i]==line[i+1]):
                return True
        return False

def hasForbiddenContent(line):
    if ("ab" in line or "cd" in line or "pq" in line or "xy" in line):
        return True
    return False

f = open('input.txt','r')
count = 0
for line in f:
    v = hasThreeVowels(line)
    d = hasDoubleLetter(line)
    f = hasForbiddenContent(line)
    output = "{l} {v} {d} {f}".format(l=line, v=hasThreeVowels(line), d=hasDoubleLetter(line), f=hasForbiddenContent(line))
    print(output)
    if (v and d and not f):
        count += 1
    print(count)
