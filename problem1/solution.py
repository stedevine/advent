f = open('input.txt','r')
data = f.read()
total = data.count('(') - data.count(')')
print(total)
