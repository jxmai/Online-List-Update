import random
import unittest
# import matplotlib.pyplot as plt
# import numpy as np
# import math

def moveToFront(sequence = [], inputList = []):
    for s in sequence:
        for i in range(len(inputList)):
            if(inputList[i] == s):
                inputList.insert(0, inputList.pop(i))
    return inputList




class TestMTF(unittest.TestCase):

    def test_MTF_1(self):
        self.assertEqual(moveToFront([1],[5,4,3,2,1]), [1,5,4,3,2])

    def test_MTF_2(self):
        self.assertEqual(moveToFront([1,2],[5,4,3,2,1]), [2,1,5,4,3])

if __name__== "__main__":
    unittest.main()