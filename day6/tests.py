from part1 import LightGrid
import pprint
import unittest

class applySwitchTest(unittest.TestCase):
    def test_turn_on(self):
        self.assertEqual(1, LightGrid.applySwitch("turn on", 0))
    def test_turn_off(self):
        self.assertEqual(0, LightGrid.applySwitch("turn off", 0))
    def test_toggle_off_on(self):
        self.assertEqual(1, LightGrid.applySwitch("toggle", 0))
    def test_toggle_on_off(self):
        self.assertEqual(0, LightGrid.applySwitch("toggle", 1))

class parseInstructionTest(unittest.TestCase):
    def test_toggle(self):
        result = LightGrid.parseInstruction("toggle 461,550 through 564,900")
        self.assertEqual('toggle', result['operation'])
        self.assertEqual(461, result['xStart'])
        self.assertEqual(550, result['yStart'])
        self.assertEqual(564, result['xEnd'])
        self.assertEqual(900, result['yEnd'])

    def test_turn_on(self):
        result = LightGrid.parseInstruction("turn on 599,989 through 806,993")
        self.assertEqual('turn on', result['operation'])
        self.assertEqual(599, result['xStart'])
        self.assertEqual(989, result['yStart'])
        self.assertEqual(806, result['xEnd'])
        self.assertEqual(993, result['yEnd'])

    def test_turn_off(self):
        result = LightGrid.parseInstruction("turn off 464,858 through 833,915")
        self.assertEqual('turn off', result['operation'])
        self.assertEqual(464, result['xStart'])
        self.assertEqual(858, result['yStart'])
        self.assertEqual(833, result['xEnd'])
        self.assertEqual(915, result['yEnd'])

class processInstruction(unittest.TestCase):
    def test_turn_on(self):
        matrix = [[0 for x in range (5)] for x in range(5)]
        LightGrid.processInstruction("turn on 1,1 through 3,3",matrix)
        self.assertEqual(0, matrix[0][0])
        self.assertEqual(0, matrix[0][1])
        self.assertEqual(0, matrix[0][2])
        self.assertEqual(0, matrix[0][3])
        self.assertEqual(0, matrix[0][4])

        self.assertEqual(0, matrix[1][0])
        self.assertEqual(1, matrix[1][1])
        self.assertEqual(1, matrix[1][2])
        self.assertEqual(1, matrix[1][3])
        self.assertEqual(0, matrix[1][4])

        self.assertEqual(0, matrix[2][0])
        self.assertEqual(1, matrix[2][1])
        self.assertEqual(1, matrix[2][2])
        self.assertEqual(1, matrix[2][3])
        self.assertEqual(0, matrix[2][4])

        self.assertEqual(0, matrix[3][0])
        self.assertEqual(1, matrix[3][1])
        self.assertEqual(1, matrix[3][2])
        self.assertEqual(1, matrix[3][3])
        self.assertEqual(0, matrix[3][4])

        self.assertEqual(0, matrix[4][0])
        self.assertEqual(0, matrix[4][1])
        self.assertEqual(0, matrix[4][2])
        self.assertEqual(0, matrix[4][3])
        self.assertEqual(0, matrix[4][4])

class count(unittest.TestCase):
    def test_turn_on(self):
        matrix = [[0 for x in range (5)] for x in range(5)]
        LightGrid.processInstruction("turn on 1,1 through 3,3",matrix)
        self.assertEqual(9, LightGrid.countOnLights(matrix))
