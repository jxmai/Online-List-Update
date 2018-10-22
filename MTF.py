import random
import unittest
import copy
# import matplotlib.pyplot as plt
# import numpy as np
# import math

# Assume no free exchanges
def moveToFront(sequence = [], inputList = []):
    totalCost = 0
    outputList = copy.deepcopy(inputList)

    for s in sequence:
        for i in range(len(outputList)):
            if(outputList[i] == s):
                totalCost += 2 * i + 1
                outputList.insert(0, outputList.pop(i))
    return outputList, totalCost

# Assume no free exchanges, and ingore the initial rearrange cost
def decreasingFreqListUpdate():
    pass


def main():
    theList = random.sample(xrange(10000),10)
    # print(theList)
    sequence = []

    # adversary sequence
    sequence = theList[::-1]
    # print(sequence)

    #random sequence (hide for now)
    # for i in range(100):
    #     sequence.append(theList[random.randint(0,len(theList)-1)])
    # print sequence
    cost = (moveToFront(sequence, theList))[1]
    print(cost)


class TestMTF(unittest.TestCase):

    def test_MTF_1(self):
        self.assertEqual(moveToFront([1],[5,4,3,2,1])[0], [1,5,4,3,2])
        self.assertEqual(moveToFront([1],[5,4,3,2,1])[1], 9)

    def test_MTF_2(self):
        self.assertEqual(moveToFront([1,2],[5,4,3,2,1])[0], [2,1,5,4,3])
        self.assertEqual(moveToFront([1,2],[5,4,3,2,1])[1], 18)

if __name__== "__main__":
    # unittest.main()
    main()