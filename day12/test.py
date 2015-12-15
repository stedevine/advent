from jsonCounter import JsonCounter
from jsonCounter import JsonCounterNoRed
import unittest

class getTotal(unittest.TestCase):
    def test_json_object(self):
        self.assertEqual(0,JsonCounter.getTotalForObject({}))
        self.assertEqual(0,JsonCounter.getTotalForObject({'a' : 'hello'}))
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

class getTotalNoRed(unittest.TestCase):
    def test_no_red(self):
        self.assertEqual(6,JsonCounterNoRed.getTotalForObjectNoRed([1,2,3]))
        self.assertEqual(4,JsonCounterNoRed.getTotalForObject([1,{"c":"red", "b": 2},3]))
        self.assertEqual(0,JsonCounterNoRed.getTotalForObjectNoRed({"d":"red","e":[1,2,3,4],"f":5}))
        self.assertEqual(6,JsonCounterNoRed.getTotalForObjectNoRed([1,"red",5]))
