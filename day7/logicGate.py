class LogicGate:

    def parseInstruction(line):
        instruction = line.split(' -> ')
        return {'input' : LogicGate.parseInput(instruction[0]), 'output': instruction[1]}

    def parseInput(input):
        command = input.split(' ')
        if (len(command) == 1):
            return {'operation' : 'SET', 'value' : command[0] }

        if (len(command) == 2):
            return {'operation' : 'NOT', 'right' : command[1] }

        if (len(command) == 3):
            operation = command[1]
            if (operation == 'LSHIFT' or operation == 'RSHIFT'):
                # right side of LSHIFT and RSHIFT is always an int in out input
                return {'operation' : operation, 'left' : command[0], 'right' : int(command[2])}
            return {'operation' : operation, 'left' : command[0], 'right' : command[2] }


    def getDigit(value, wireSignalMap):
        if value.isdigit():
            return int(value)

        if (value in wireSignalMap):
            return int(wireSignalMap[value])

        return None

    def processCommandList(commands, wireSignalMap):
        # find the signal value for the wire a
        # we may have to loop through the list of commands multiple times until a is set (all the inputs to a must be set!)
        solvedGates = 0
        while not 'a' in wireSignalMap:
            #print (len(commands))
            #print (commands[0]['input']['operation'])
            for i in range(len(commands)):
                #print("total {t} solved {s}".format(t=len(commands), s=solvedGates))
            #for c in commands:
                #print(c)
                #print (commands[i])
                operation = commands[i]['input']['operation']
                output = commands[i]['output']
                if (output not in wireSignalMap):
                    if operation == 'SET':
                        value = LogicGate.getDigit(commands[i]['input']['value'],wireSignalMap)
                        if value is not None :
                            wireSignalMap.update({output:int(value)})
                            solvedGates += 1
                            text = "wire {w} = {v}".format(w=output, v=int(value))
                            print(text)

                    if (operation == 'AND' or operation == 'OR'):
                        left = LogicGate.getDigit(commands[i]['input']['left'], wireSignalMap)
                        right = LogicGate.getDigit(commands[i]['input']['right'], wireSignalMap)
                        if (left is not None and right is not None):
                            if (operation == 'AND'):
                                #value = wireSignalMap[left] & wireSignalMap[right] & 65535
                                value = left & right & 65535
                                wireSignalMap.update({output:(value)})
                                solvedGates += 1
                                #text = "{leftwire}({l}) {op} {rightwire}({r}) sets wire {w} = {v}".format(leftwire=left, l=wireSignalMap[left], op=operation, rightwire=right, r=wireSignalMap[right],  w=output, v=value)
                                #print(text)
                            elif (operation == 'OR'):
                                value = left | right & 65535
                                wireSignalMap.update({output:(value)})
                                solvedGates += 1
                                #text = "{leftwire}({l}) {op} {rightwire}({r}) sets wire {w} = {v}".format(leftwire=left, l=wireSignalMap[left], op=operation, rightwire=right, r=wireSignalMap[right],  w=output, v=value)
                                #print(text)
                            continue

                    if (operation == 'LSHIFT' or operation == 'RSHIFT'):
                        left = commands[i]['input']['left']
                        right = commands[i]['input']['right']
                        if (left in wireSignalMap):
                            if (operation == 'LSHIFT'):
                                #print(wireSignalMap)
                                value = wireSignalMap[left] << right & 65535
                                wireSignalMap.update({output:(value)})
                                solvedGates += 1
                                text = "{leftwire}({l}) {op} {rightwire} sets wire {w} = {v}".format(leftwire=left, l=wireSignalMap[left], op=operation, rightwire=right,  w=output, v=value)
                                print(text)
                            elif (operation == 'RSHIFT'):
                                value = wireSignalMap[left] >> right & 65535
                                wireSignalMap.update({output:(value)})
                                solvedGates += 1
                                text = "{leftwire}({l}) {op} {rightwire} sets wire {w} = {v}".format(leftwire=left, l=wireSignalMap[left], op=operation, rightwire=right,  w=output, v=value)
                                print(text)
                            continue


                    if operation == 'NOT':
                        right = commands[i]['input']['right']
                        if right in wireSignalMap:
                            value = ~wireSignalMap[right] & 65535
                            wireSignalMap.update({output:value})
                            solvedGates += 1
                            text = "{op} {rightwire}({r}) sets wire {w} = {v}".format(op=operation, rightwire=right, r=wireSignalMap[right],  w=output, v=value)
                            print(text)
            #print(wireSignalMap['a'])
