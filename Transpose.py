import unittest
import copy

def accessTranspose(sequence = [], inputList = []):
    outputList = copy.deepcopy(inputList)
    
    totalCost = 0
    totalCostsForEachAccessList = []

    for s in sequence:
        for i in range(len(outputList)):
            if outputList[i] == s:
                totalCost += i + 1
                if i != 0:
                    outputList.insert(i-1, outputList.pop(i))
                    totalCost += 1
                totalCostsForEachAccessList.append(totalCost)
    
    return outputList, totalCost, totalCostsForEachAccessList

class TestTranspose(unittest.TestCase):
    def test_transpose_1(self):
        self.assertEqual(accessTranspose([5], [1,2,3,4,5])[0], [1,2,3,5,4])
        self.assertEqual(accessTranspose([5], [1,2,3,4,5])[1], 6)
        self.assertEqual(accessTranspose([5], [1,2,3,4,5])[2], [6])

    def test_transpose_2(self):
        self.assertEqual(accessTranspose([5,5], [1,2,3,4,5])[0], [1,2,5,3,4])
        self.assertEqual(accessTranspose([5,5], [1,2,3,4,5])[1], 6 + 5)
        self.assertEqual(accessTranspose([5,5], [1,2,3,4,5])[2], [6, 11])

    def test_transpose_3(self):
        self.assertEqual(accessTranspose([5,5,2], [1,2,3,4,5])[0], [2,1,5,3,4])
        self.assertEqual(accessTranspose([5,5,2], [1,2,3,4,5])[1], 6 + 5 + 3)
        self.assertEqual(accessTranspose([5,5,2], [1,2,3,4,5])[2], [6, 11, 14])

    def test_transpose_4(self):
        self.assertEqual(accessTranspose([5,5,2,2], [1,2,3,4,5])[0], [2,1,5,3,4])
        self.assertEqual(accessTranspose([5,5,2,2], [1,2,3,4,5])[1], 6 + 5 + 3 + 1)
        self.assertEqual(accessTranspose([5,5,2,2], [1,2,3,4,5])[2], [6, 11, 14, 15])

if __name__== "__main__":
    unittest.main()