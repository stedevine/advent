class LightGrid:

    def processInstruction(line, matrix):
        instruction = LightGrid.parseInstruction(line)
        # assume an n x n matrix
        n = len(matrix[0])
        for i in range(instruction['xStart'], instruction['xEnd']+1):
            for j in range(instruction['yStart'], instruction['yEnd']+1):
                matrix[i][j] = LightGrid.applySwitch(instruction['operation'], matrix[i][j])

        return matrix

    def parseInstruction(line):
        # example input:
        #turn on 606,361 through 892,600
        #turn off 448,208 through 645,684
        #toggle 50,472 through 452,788
        input = line.split(' ')
        if (len(input) == 4) :
            start = input[1].split(',')
            end = input[3].split(',')
            return { 'operation' : input[0], 'xStart' : int(start[0]), 'yStart' : int(start[1]), 'xEnd' : int(end[0]), 'yEnd' : int(end[1]) }
        else:
            start = input[2].split(',')
            end = input[4].split(',')
            return { 'operation' : input[0] + " " + input[1], 'xStart' : int(start[0]), 'yStart' : int(start[1]), 'xEnd' : int(end[0]), 'yEnd' : int(end[1]) }

    def applySwitch(operation, existingValue):
        if operation == "turn on":
            return 1
        elif operation == "turn off":
            return 0
        else:
            if existingValue == 0:
                return 1
        return 0

    def countOnLights(matrix):
        count = 0
        # assume an n x n matrix
        n = len(matrix[0])
        for i in range(0, n):
            for j in range(0, n):
                count += matrix[i][j]
        return count
