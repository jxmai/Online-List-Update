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
    return outputList


class TestDFC(unittest.TestCase):
    def test_DFC_1(self):
        self.assertEqual(accessDecreasingFreqList([1],[5,4,3,2,1]), [1,5,4,3,2])

    def test_DFC_1(self):
        self.assertEqual(accessDecreasingFreqList([1,2],[5,4,3,2,1]), [1,2,5,4,3])

if __name__== "__main__":
    unittest.main()