def process(program, a, b):
    # map the instruction to a function that executes the function
    # functions will return the value of the register and the new offset
    d = {}

    # Always change the reg value and increment the offset by 1 (ignore the jmp value)
    d['inc'] = lambda reg, offset, jmp : (reg + 1, offset + 1)
    d['tpl'] = lambda reg, offset, jmp : (reg * 3, offset + 1)
    d['hlf'] = lambda reg, offset, jmp : (int(reg / 2), offset + 1)
    
    # Never change the reg value, increment the offset by 1 or the jmp value
    d['jmp'] = lambda reg, offset, jmp : (reg, offset + jmp)
    d['jie'] = lambda reg, offset, jmp : (reg, offset + jmp if reg % 2 == 0 else offset + 1)
    d['jio'] = lambda reg, offset, jmp : (reg, offset + jmp if reg == 1 else offset + 1)

    offset = 0
    while offset < len(program):
        # parse each line in the input program
        tokens = program[offset].split(' ')
        instruction = tokens[0]
        # special case for jmp instruction
        if instruction == 'jmp':
            jmp = tokens[1]
            register = None
        else:
            register = tokens[1].strip(',').strip()
            #print('register :{}:'.format(register))
            jmp = 0
            if len(tokens) == 3:
                jmp = tokens[2]

        if register == 'a':
            a, offset = d[instruction](a, offset, int(jmp))
        else:
            b, offset = d[instruction](b, offset, int(jmp))
        
    return (a,b)

'''
input = [
'inc a',
'jio a, +2',
'tpl a',
'inc a'
]

print(process(input))
'''

with open('./input.txt') as f:
    lines = f.readlines()
    # problem1
    print(process(program=lines, a=0, b=0))
    # problem2
    print(process(program=lines, a=1, b=0))
    