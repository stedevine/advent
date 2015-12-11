from memoryString import MemoryString

# compare the length of the string in code to the encoded length of the string:
# string is always quoted: "string"
# string can contain:
#   quotes " --> \"
#   slashes \ --> \\

totalUnencodedLength = 0
totalEncodedLength = 0
f = open('input.txt','r')
for line in f:
    trimmed = line.strip()
    result = MemoryString.countEncodedCharacters(trimmed)
    #text = "{l} {code} {memory}".format(l=trimmed, code=result['codeCharacters'], memory=result['memoryCharacters'])
    #print(text)
    totalUnencodedLength += result['unencodedCharacters']
    totalEncodedLength +=  result['encodedCharacters']

print(totalUnencodedLength)
print(totalEncodedLength)
print(totalEncodedLength - totalUnencodedLength)
