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


    def processCommandList(commands, wireSignalMap):
        # find the signal value for the wire a
        # we may have to loop through the list of commands multiple times until a is set (all the inputs to a must be set!)
        while not 'a' in wireSignalMap:
            print (len(commands))
            print (commands[0]['input']['operation'])
            for i in range(len(commands)):
            #for c in commands:
                #print(c)
                print (commands[i])
                operation = commands[i]['input']['operation']
                output = commands[i]['output']

                if operation == 'SET':
                    value = commands[i]['input']['value']
                    if value.isdigit() :
                        wireSignalMap.update({output:int(value)})
                    elif (value in wireSignalMap):
                        wireSignalMap.update({output:wireSignalMap[value]})
                    continue

                if (operation == 'AND' or operation == 'OR'):
                    left = commands[i]['input']['left']
                    right = commands[i]['input']['right']
                    if (left in wireSignalMap and right in wireSignalMap):
                        if (operation == 'AND'):
                            wireSignalMap.update({output:(wireSignalMap[left] & wireSignalMap[right] & 65535)})
                        elif (operation == 'OR'):
                            wireSignalMap.update({output:(wireSignalMap[left] | wireSignalMap[right] & 65535)})
                    continue

                if (operation == 'LSHIFT' or operation == 'RSHIFT'):
                    left = commands[i]['input']['left']
                    right = commands[i]['input']['right']
                    if (left in wireSignalMap):
                        if (operation == 'LSHIFT'):
                            print(wireSignalMap)
                            wireSignalMap.update({output:(wireSignalMap[left] << right & 65535)})
                        elif (operation == 'RSHIFT'):
                            wireSignalMap.update({output:(wireSignalMap[left] >> right & 65535)})
                    continue


                if operation == 'NOT':
                    right = commands[i]['input']['right']
                    if right in wireSignalMap:
                        wireSignalMap.update({output:~wireSignalMap[right] & 65535})

        #print(wireSignalMap['a'])
