class LogicGate:

    def parseInstruction(line):
        instruction = line.split(' -> ')
        return {'input' : LogicGate.parseInput(instruction[0]), 'output': instruction[1]}

    def parseInput(input):
        command = input.split(' ')
        if (len(command) == 1):
            return {'operation' : 'SET', 'value' : int(command[0]) }

        if (len(command) == 2):
            return {'operation' : 'NOT', 'right' : command[1] }

        if (len(command) == 3):
            operation = command[1]
            if (operation == 'LSHIFT' or operation == 'RSHIFT'):
                return {'operation' : operation, 'left' : command[0], 'right' : int(command[2])}
            return {'operation' : operation, 'left' : command[0], 'right' : command[2] }


    def processCommandList(commands, wireSignalMap):
        # find the signal value for the wire a
        # we may have to loop through the list of commands multiple times until a is set (all the inputs to a must be set!)
        while not 'a' in wireSignalMap:
            for c in commands:
                operation = c['input']['operation']
                output = c['output']

                if (operation == 'SET'):
                    wireSignalMap.update({output:c['input']['value']})
                    continue

                if (operation == 'AND'):
                    left = c['input']['left']
                    right = c['input']['right']
                    if (left in wireSignalMap and right in wireSignalMap):
                        wireSignalMap.update({output:(wireSignalMap[left] & wireSignalMap[right])})

        #print(wireSignalMap['a'])
