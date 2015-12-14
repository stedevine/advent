from password import Password
import unittest

class incrementPassword(unittest.TestCase):
    def test_non_rollover(self):
        result = Password.increment("aaaaaaaa")
        self.assertEqual("aaaaaaab", result)

    def test_one_rollover(self):
        result = Password.increment("aaaaaaaz")
        self.assertEqual("aaaaaaba", result)

    def test_multiple_rollover(self):
        result = Password.increment("aaaazzzz")
        self.assertEqual("aaabaaaa", result)

    def test_total_rollover(self):
        result = Password.increment("zzzzzzzz")
        self.assertEqual("aaaaaaaa", result)

class hasIncreasingStraightOfThree(unittest.TestCase):
    def test_no_straight(self):
        self.assertEqual(False, Password.hasIncreasingStraightOfThree("abababab"))

    def test_first_chars_increasing_straight(self):
        self.assertEqual(True, Password.hasIncreasingStraightOfThree("abcaaaaa"))

    def test_last_chars_increasing_straight(self):
        self.assertEqual(True, Password.hasIncreasingStraightOfThree("aaaaaghi"))

    def test_mid_chars_increasing_straight(self):
        self.assertEqual(True, Password.hasIncreasingStraightOfThree("bbbxyzaa"))

    def test_chars_have_leading_y_and_z_straight(self):
        self.assertEqual(True, Password.hasIncreasingStraightOfThree("xzyxyzaa"))

    def test_problem_input(self):
        self.assertEqual(True, Password.hasIncreasingStraightOfThree("hijklmmn"))
        self.assertEqual(False, Password.hasIncreasingStraightOfThree("abbceffg"))


class containsInvalidCharacter(unittest.TestCase):
    def test_i(self):
        self.assertEqual(True, Password.containsInvalidCharacter("aaaiaaaa"))

    def test_o(self):
        self.assertEqual(True, Password.containsInvalidCharacter("aaaoaaaa"))

    def test_l(self):
        self.assertEqual(True, Password.containsInvalidCharacter("aaalaaaa"))

    def test_valid(self):
        self.assertEqual(False, Password.containsInvalidCharacter("aaabaaaa"))

    def test_problem_input(self):
        self.assertEqual(True, Password.containsInvalidCharacter("hijklmmn"))


class containTwoPairsOfLetters(unittest.TestCase):
    def test_has_two_pairs(self):
        self.assertEqual(True, Password.containTwoPairsOfLetters("aabbqwer"))
        self.assertEqual(True, Password.containTwoPairsOfLetters("aaxbbqwe"))
        self.assertEqual(True, Password.containTwoPairsOfLetters("bbqweraa"))
        self.assertEqual(True, Password.containTwoPairsOfLetters("qwerxxaa"))

    def test_not_has_two_pairs(self):
        self.assertEqual(False, Password.containTwoPairsOfLetters("aaaaaaaa"))
        self.assertEqual(False, Password.containTwoPairsOfLetters("aaaaaaab"))
        self.assertEqual(False, Password.containTwoPairsOfLetters("baaaaaab"))
        self.assertEqual(False, Password.containTwoPairsOfLetters("abababab"))
        self.assertEqual(False, Password.containTwoPairsOfLetters("aaaacbaa"))

    def test_problem_input(self):
        self.assertEqual(True, Password.containTwoPairsOfLetters("abbceffg"))
        self.assertEqual(False, Password.containTwoPairsOfLetters("abbcegjk"))

class isValid(unittest.TestCase):
    def test_from_problem(self):
        self.assertEqual(True, Password.isValid("abcdffaa"))

class getNextPassword(unittest.TestCase):
    def test_from_problem(self):
        self.assertEqual("abcdffaa", Password.getNextPassword("abcdefgh"))
        # takes 3 minutes to run 
        self.assertEqual("ghjaabcc", Password.getNextPassword("ghijklmn"))
