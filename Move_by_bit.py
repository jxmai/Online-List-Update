import unittest

# Assume no free exchanges
def move_by_bit(sequence = [], inputList = []):
    totalCost = 0
    outputList = inputList[:]
    totalCostsForEachAccessList = []
    bitList = [0] * len(inputList)
    for s in sequence:
        item_index = outputList.index(s)
        if bitList[item_index] == 0:
            bitList[item_index] = 1
            totalCost += item_index+1
        else:
            bitList[item_index] = 0
            totalCost += (2 * item_index) + 1
            outputList.insert(0, outputList.pop(item_index))
            bitList.insert(0, bitList.pop(item_index))
        totalCostsForEachAccessList.append(totalCost)
    return outputList, totalCost, totalCostsForEachAccessList


class Test_MBB(unittest.TestCase):

    def test_MTF_1(self):
        self.assertEqual(move_by_bit([1],[5,4,3,2,1])[0], [5,4,3,2,1])
        self.assertEqual(move_by_bit([1],[5,4,3,2,1])[1], 5)

    def test_MTF_2(self):
        self.assertEqual(move_by_bit([1,1],[5,4,3,2,1])[0], [1,5,4,3,2])
        self.assertEqual(move_by_bit([1,1],[5,4,3,2,1])[1], 5+5+4)  # access cost + access cost + switch cost
        self.assertEqual(move_by_bit([1,1],[5,4,3,2,1])[2], [5, 14])


if __name__== "__main__":
    unittest.main()
