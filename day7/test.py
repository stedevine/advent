from logicGate import LogicGate
import unittest

class parseInstructionTest(unittest.TestCase):
    def test_parse_set_operation(self):
        result = LogicGate.parseInstruction('123 -> x')
        self.assertEqual('SET', result['input']['operation'])
        self.assertEqual('123', result['input']['value'])
        self.assertEqual('x', result['output'])
    def test_parse_not_operation(self):
        result = LogicGate.parseInstruction('NOT a -> x')
        self.assertEqual('NOT', result['input']['operation'])
        self.assertEqual('a', result['input']['right'])
        self.assertEqual('x', result['output'])
    def test_parse_two_input_operation(self):
        result = LogicGate.parseInstruction('p LSHIFT 2 -> z')
        self.assertEqual('LSHIFT', result['input']['operation'])
        self.assertEqual('p', result['input']['left'])
        self.assertEqual(2, result['input']['right'])
        self.assertEqual('z', result['output'])

class parseInputTest(unittest.TestCase):
    def test_parse_intput_set_operation(self):
        result = LogicGate.parseInput('123')
        self.assertEqual('123', result['value'])
        self.assertEqual('SET', result['operation'])
    def test_parse_intput_not_operation(self):
        result = LogicGate.parseInput('NOT z')
        self.assertEqual('z', result['right'])
        self.assertEqual('NOT', result['operation'])
    def test_parse_intput_lshift_operation(self):
        result = LogicGate.parseInput('y LSHIFT 23')
        self.assertEqual('LSHIFT', result['operation'])
        self.assertEqual('y', result['left'])
        self.assertEqual(23, result['right'])
    def test_parse_intput_rshift_operation(self):
        result = LogicGate.parseInput('z RSHIFT 2')
        self.assertEqual('RSHIFT', result['operation'])
        self.assertEqual('z', result['left'])
        self.assertEqual(2, result['right'])
    def test_parse_intput_and_operation(self):
        result = LogicGate.parseInput('z AND y')
        self.assertEqual('AND', result['operation'])
        self.assertEqual('z', result['left'])
        self.assertEqual('y', result['right'])
    def test_parse_intput_or_operation(self):
        result = LogicGate.parseInput('a OR b')
        self.assertEqual('OR', result['operation'])
        self.assertEqual('a', result['left'])
        self.assertEqual('b', result['right'])

class processCommandList(unittest.TestCase):
    def test_set_operation_constant(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('123 -> a'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(123, wireSignalMap['a'])

    def test_set_operation_variable(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('x -> a'))
        commands.append(LogicGate.parseInstruction('123 -> x'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(123, wireSignalMap['a'])

    def test_and_operation_with_inputs_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('6 -> x'))
        commands.append(LogicGate.parseInstruction('13 -> y'))
        commands.append(LogicGate.parseInstruction('x AND y -> a'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(4, wireSignalMap['a'])
    def test_and_operation_with_no_inputs_initially_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('x AND y -> a'))
        commands.append(LogicGate.parseInstruction('6 -> x'))
        commands.append(LogicGate.parseInstruction('13 -> y'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(4, wireSignalMap['a'])
    def test_and_operation_with_one_input_initially_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('6 -> x'))
        commands.append(LogicGate.parseInstruction('x AND y -> a'))
        commands.append(LogicGate.parseInstruction('13 -> y'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(False, 'c' in wireSignalMap)

    def test_or_operation_with_inputs_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('6 -> x'))
        commands.append(LogicGate.parseInstruction('13 -> y'))
        commands.append(LogicGate.parseInstruction('x OR y -> a'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(15, wireSignalMap['a'])

    def test_lshift_operation_with_input_not_initially_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('x LSHIFT 2 -> a'))
        commands.append(LogicGate.parseInstruction('6 -> x'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(24, wireSignalMap['a'])

    def test_lshift_operation_with_input_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('6 -> x'))
        commands.append(LogicGate.parseInstruction('x LSHIFT 2 -> a'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(24, wireSignalMap['a'])

    def test_rshift_operation_with_input_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('6 -> x'))
        commands.append(LogicGate.parseInstruction('x RSHIFT 4 -> a'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(0, wireSignalMap['a'])

    def test_not_operation_with_input_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('24 -> y'))
        commands.append(LogicGate.parseInstruction('NOT y -> a'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(65511, wireSignalMap['a'])
    def test_not_operation_with_input_not_initially_set(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('NOT y -> a'))
        commands.append(LogicGate.parseInstruction('101 -> y'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(65434, wireSignalMap['a'])

    # python -m unittest test.processCommandList.test_puzzle_input
    def test_puzzle_input(self):
        wireSignalMap = {}
        commands = []
        commands.append(LogicGate.parseInstruction('123 -> x'))
        commands.append(LogicGate.parseInstruction('456 -> y'))
        commands.append(LogicGate.parseInstruction('x AND y -> d'))
        commands.append(LogicGate.parseInstruction('x OR y -> e'))
        commands.append(LogicGate.parseInstruction('x LSHIFT 2 -> f'))
        commands.append(LogicGate.parseInstruction('y RSHIFT 2 -> g'))
        commands.append(LogicGate.parseInstruction('NOT x -> h'))
        commands.append(LogicGate.parseInstruction('NOT y -> a'))
        LogicGate.processCommandList(commands, wireSignalMap)
        self.assertEqual(72, wireSignalMap['d'])
        self.assertEqual(507, wireSignalMap['e'])
        self.assertEqual(492, wireSignalMap['f'])
        self.assertEqual(114, wireSignalMap['g'])
        self.assertEqual(65412, wireSignalMap['h'])
        self.assertEqual(65079, wireSignalMap['a'])
        self.assertEqual(123, wireSignalMap['x'])
        self.assertEqual(456, wireSignalMap['y'])
