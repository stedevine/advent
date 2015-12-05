import hashlib
#find the lowest number that creates an MD5 hash that stats with 000000
#for the input bgvyzdsv<number>

inputtext = "bgvyzdsv"

for number in range(1000000000):

    text = "{text}{number}".format(text=inputtext,number=number)
    m = hashlib.md5()
    text = text.encode('utf-8')
    m.update(text)
    h = m.hexdigest()
    if (h.startswith('000000')):
        print(number)
        break
    output = "{text} : {hash}".format(text=text, hash=h)
    if (number % 10000000 == 0):
        print(output)
