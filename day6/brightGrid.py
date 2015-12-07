from lightGrid import LightGrid

class BrightGrid:

    def processInstruction(line, matrix):
        instruction = LightGrid.parseInstruction(line)
        # assume an n x n matrix
        n = len(matrix[0])
        for i in range(instruction['xStart'], instruction['xEnd']+1):
            for j in range(instruction['yStart'], instruction['yEnd']+1):
                matrix[i][j] = BrightGrid.applySwitch(instruction['operation'], matrix[i][j])

        return matrix

    def applySwitch(operation, existingValue):
        if operation == "turn on":
            return existingValue + 1
        elif operation == "turn off":
            return max(0,existingValue - 1)
        else:
            return existingValue + 2

    def countTotalBrightness(matrix):
        count = 0
        # assume an n x n matrix
        n = len(matrix[0])
        for i in range(0, n):
            for j in range(0, n):
                count += matrix[i][j]
        return count
