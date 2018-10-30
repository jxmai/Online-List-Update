import unittest

# Assume no free exchanges
def moveToFront(sequence = [], inputList = []):
    totalCost = 0
    totalCostsForEachAccessList = []
    outputList = inputList[:]

    for s in sequence:
        item_index = outputList.index(s)
        totalCost += (2 * item_index) + 1
        totalCostsForEachAccessList.append(totalCost)
        outputList.insert(0, outputList.pop(item_index))
    return outputList, totalCost, totalCostsForEachAccessList

class TestMTF(unittest.TestCase):

    def test_MTF_1(self):
        self.assertEqual(moveToFront([1],[5,4,3,2,1])[0], [1,5,4,3,2])
        self.assertEqual(moveToFront([1],[5,4,3,2,1])[1], 9)
        self.assertEqual(moveToFront([1],[5,4,3,2,1])[2], [9])

    def test_MTF_2(self):
        self.assertEqual(moveToFront([1,2],[5,4,3,2,1])[0], [2,1,5,4,3])
        self.assertEqual(moveToFront([1,2],[5,4,3,2,1])[1], 18)
        self.assertEqual(moveToFront([1,2],[5,4,3,2,1])[2], [9,18])

if __name__== "__main__":
    unittest.main()