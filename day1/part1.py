# To what floor do the instructions send santa?
# ( -> move up
# ) -> move down
f = open('input.txt','r')
data = f.read()
total = data.count('(') - data.count(')')
print(total)
