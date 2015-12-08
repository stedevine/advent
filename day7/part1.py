# day 7 logic gates
# given input of the form:
# x AND y -> z
# where x and y are inputs that carry a 16 bit number,
# AND is one of several supported operations
# z is the output

def parseInstruction(line):
    instruction = line.split(' -> ')
    return {'input' : instruction[0], 'output': instruction[1]}

parseInstruction("123 -> x")
parseInstruction("x AND y -> z")
parseInstruction("NOT e -> f")
