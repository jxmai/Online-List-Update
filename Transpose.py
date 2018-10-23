import unittest
import copy

def accessTranspose(sequence = [], inputList = []):
    outputList = copy.deepcopy(inputList)
    
    for s in sequence:
        for i in range(len(outputList)):
            if outputList[i] == s:
                if i != 0:
                    outputList.insert(i-1, outputList.pop(i))
    
    return outputList




class TestTranspose(unittest.TestCase):
    def test_transpose_1(self):
        self.assertEqual(accessTranspose([5], [1,2,3,4,5]), [1,2,3,5,4])

    def test_transpose_2(self):
        self.assertEqual(accessTranspose([5,5], [1,2,3,4,5]), [1,2,5,3,4])

    def test_transpose_3(self):
        self.assertEqual(accessTranspose([5,5,2], [1,2,3,4,5]), [2,1,5,3,4])

    def test_transpose_4(self):
        self.assertEqual(accessTranspose([5,5,2,2], [1,2,3,4,5]), [2,1,5,3,4])

if __name__== "__main__":
    unittest.main()