from jsonCounter import JsonCounter
import unittest

class getTotal(unittest.TestCase):
    def test_json_object(self):
        self.assertEqual(0,JsonCounter.getTotalForObject({}))
        self.assertEqual(0,JsonCounter.getTotalForObject({'a' : 0}))
        self.assertEqual(0,JsonCounter.getTotalForObject({'a' : 0, 'b' : 0}))
        self.assertEqual(6,JsonCounter.getTotalForObject({'a' : 1, 'b' : 2, 'c' : 3}))

    def test_json_object_sub_object(self):
        self.assertEqual(1,JsonCounter.getTotalForObject({'a' : {'b': 1}}))
        self.assertEqual(1,JsonCounter.getTotalForObject({'a' : {'b': { 'c' : 1}}}))
        self.assertEqual(3,JsonCounter.getTotalForObject({'a' : {'b': { 'c' : 1, 'd' : 2}}}))
        self.assertEqual(3,JsonCounter.getTotalForObject({'a' : 1, 'b': {'c' : 2}}))
        self.assertEqual(6,JsonCounter.getTotalForObject({'a' : 1, 'b': {'c' : 2, 'd' :{'e' : 3}}}))

    def test_json_array_of_numbers(self):
        self.assertEqual(1,JsonCounter.getTotalForObject([1]))
        self.assertEqual(6,JsonCounter.getTotalForObject({'a' : [1,2,3]}))

    def test_json_array_of_objects(self):
        self.assertEqual(3,JsonCounter.getTotalForObject([{'b' :1, 'c' :2}]))
        self.assertEqual(3,JsonCounter.getTotalForObject({'a' : [{'b' :1, 'c' :2}]}))

    def test_json_array_of_arrays(self):
        self.assertEqual(3,JsonCounter.getTotalForObject({'a' : [{'b' :1, 'c' :2}]}))
        self.assertEqual(3,JsonCounter.getTotalForObject([[3]]))
