def countMemoryCharacters(stripped):
    memoryCharacters = 0
    for i in range(1, len(stripped) -1):
        #print(stripped[i])
        if (stripped[i] == "\\") :
            if (stripped[i+1] == "\\" or stripped[i+1] == "\""):
                i += 1
            else :
                print("is ascii")
                i = i + 3
                # is ascii \x12
                #i += 3
        else :
            print(stripped[i])
            memoryCharacters += 1
    return memoryCharacters

# string is always quoted: "string"
# codeLength = len(trimmed)

# mem = len(string) - 2
# for c in string
# if c == '\'
# find end of escaped string
# if is escaped quote \"
# is escaped backslash \\
# is ascii \x12
totalCodeLength = 0
totalMemoryLength = 0
f = open('single.txt','r')
for line in f:
    trimmed = line.strip()
    codeLength = len(trimmed)
    memoryLength = countMemoryCharacters(trimmed)
    text = "{l} {code} {memory}".format(l=trimmed, code=codeLength, memory=memoryLength)
    print(text)
    totalCodeLength += codeLength
    totalMemoryLength += memoryLength

print(totalCodeLength)
print(totalMemoryLength)
print(totalCodeLength - totalMemoryLength)
