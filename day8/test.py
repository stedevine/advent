from memoryString import MemoryString
import unittest

class memoryCharactersTest(unittest.TestCase):
    def test_empty_string(self):
        input = "\"\""
        print(input)
        result = MemoryString.countCharacters(input)
        print(result)
        self.assertEqual(0, result['memoryCharacters'])
        self.assertEqual(2, result['codeCharacters'])

    def test_abc_string(self):
        input = "\"abc\""
        print(input)
        result = MemoryString.countCharacters(input)
        print(result)
        self.assertEqual(3, result['memoryCharacters'])
        self.assertEqual(5, result['codeCharacters'])

    def test_escaped_quote_string(self):
        input = "\"aaa\\\"aaa\""
        print(input)
        result = MemoryString.countCharacters(input)
        print(result)
        self.assertEqual(7, result['memoryCharacters'])
        self.assertEqual(10, result['codeCharacters'])

    def test_escaped_ascii_string(self):
        input = "\"\\x27\""
        print(input)
        result = MemoryString.countCharacters(input)
        print(result)
        self.assertEqual(1, result['memoryCharacters'])
        self.assertEqual(6, result['codeCharacters'])

class encodedCharactersTest(unittest.TestCase):
    def test_empty_string(self):
        input = "\"\""
        print(input)
        result = MemoryString.countEncodedCharacters(input)
        print(result)
        self.assertEqual(2, result['unencodedCharacters'])
        self.assertEqual(6, result['encodedCharacters'])

    def test_abc_string(self):
        input = "\"abc\""
        print(input)
        result = MemoryString.countEncodedCharacters(input)
        print(result)
        self.assertEqual(5, result['unencodedCharacters'])
        self.assertEqual(9, result['encodedCharacters'])

    def test_escaped_quote_string(self):
        input = "\"aaa\\\"aaa\""
        print(input)
        result = MemoryString.countEncodedCharacters(input)
        print(result)
        self.assertEqual(10, result['unencodedCharacters'])
        self.assertEqual(16, result['encodedCharacters'])

    def test_escaped_ascii_string(self):
        input = "\"\\x27\""
        print(input)
        result = MemoryString.countEncodedCharacters(input)
        print(result)
        self.assertEqual(6, result['unencodedCharacters'])
        self.assertEqual(11, result['encodedCharacters'])
