from memoryString import MemoryString

# compare the length of the string in code to the length of the string in memory:
# string is always quoted: "string"
# string can contain:
#   escaped quotes \"
#   escaped slashes \\
#   single ascii characters expressed as \x{0-f}{0-f}
#  "" is 2 characters of code and 0 characters in memory
#  "aaa\"aaa" is 10 characters of code and 7 characters of memory

totalCodeLength = 0
totalMemoryLength = 0
f = open('input.txt','r')
for line in f:
    trimmed = line.strip()
    result = MemoryString.countCharacters(trimmed)
    #text = "{l} {code} {memory}".format(l=trimmed, code=result['codeCharacters'], memory=result['memoryCharacters'])
    #print(text)
    totalCodeLength += result['codeCharacters']
    totalMemoryLength += result['memoryCharacters']

print(totalCodeLength)
print(totalMemoryLength)
print(totalCodeLength - totalMemoryLength)
