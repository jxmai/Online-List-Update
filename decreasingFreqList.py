import unittest
import copy
import itertools
from collections import Counter

# Assume no free exchanges, and ingore the initial rearrange cost
def accessDecreasingFreqList(sequence = [], inputList = []):
    cnt = Counter()
    outputList = copy.deepcopy(inputList)

    # initialze counter
    for o in outputList:
        if o not in cnt:
            cnt[o] = 0

    totalCost = 0
    for s in sequence:
        for i in range(len(outputList)):
            if(outputList[i] == s):
                popped = outputList.pop(i)
                # access cost
                totalCost += i + 1

                cnt[popped] += 1
                previousIndex = i - 1

                inserted = False
                while previousIndex >= 0:
                    if cnt[outputList[previousIndex]] >= cnt[popped]:
                        outputList.insert(previousIndex + 1, popped)
                        inserted = True
                        break
                    previousIndex = previousIndex - 1
                if not inserted:
                    outputList.insert(0, popped)
                    totalCost += i
                else:
                    totalCost += i - previousIndex - 1

    return outputList, totalCost


class TestDFC(unittest.TestCase):
    def test_DFC_1(self):
        self.assertEqual(accessDecreasingFreqList([1],[5,4,3,2,1])[0], [1,5,4,3,2])
        self.assertEqual(accessDecreasingFreqList([1],[5,4,3,2,1])[1], 9)

    def test_DFC_2(self):
        self.assertEqual(accessDecreasingFreqList([1,2],[5,4,3,2,1])[0], [1,2,5,4,3])
        self.assertEqual(accessDecreasingFreqList([1,2],[5,4,3,2,1])[1], 9 + 8)

    def test_DFC_3(self):
        self.assertEqual(accessDecreasingFreqList([1,2,2],[5,4,3,2,1])[0], [2,1,5,4,3])
        self.assertEqual(accessDecreasingFreqList([1,2,2],[5,4,3,2,1])[1], 9 + 8 + 3)
    
    def test_DFC_4(self):
        self.assertEqual(accessDecreasingFreqList([1,2,2,5],[5,4,3,2,1])[0], [2,1,5,4,3])
        self.assertEqual(accessDecreasingFreqList([1,2,2,5],[5,4,3,2,1])[1], 9 + 8 + 3 + 3)

    def test_DFC_5(self):
        self.assertEqual(accessDecreasingFreqList([1,2,2,5,5],[5,4,3,2,1])[0], [2,5,1,4,3])

    def test_DFC_6(self):
        self.assertEqual(accessDecreasingFreqList([1,2,2,5,5,3,3,3,3],[5,4,3,2,1])[0], [3,2,5,1,4])

if __name__== "__main__":
    unittest.main()