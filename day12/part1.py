from jsonCounter import JsonCounter

f = open('input.json','r')
data = f.read()
#print(data)
print(JsonCounter.getTotalForObject(data))
