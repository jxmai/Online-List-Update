import collections as c
import unittest

# Assume no free exchanges
def static_opt(sequence = [], inputList = []):
    totalCost = 0
    outputList = inputList[:]
    totalCostsForEachAccessList = []
    counts = c.Counter(sequence)

    insert_index = 0
    # order by frequency
    for i in counts.most_common():
        item_index = outputList.index(i[0])     # i = (item, frequency)
        # number of switches
        assert item_index >= insert_index
        totalCost += item_index - insert_index
        outputList.insert(insert_index, outputList.pop(item_index))
        insert_index += 1

    totalCostsForEachAccessList.append(totalCost)
    #check if ordered correctly
    #assert outputList == [i[0] for i in counts.most_common()]

    for s in sequence:
        totalCost += outputList.index(s)+1
        totalCostsForEachAccessList.append(totalCost)

    return outputList, totalCost, totalCostsForEachAccessList


class Test_Static_OPT(unittest.TestCase):

    def test_Static_OPT_1(self):
        self.assertEqual(static_opt([1],[5,4,3,2,1])[0], [1,5,4,3,2])
        self.assertEqual(static_opt([1],[5,4,3,2,1])[1], 5)

    def test_Static_OPT_2(self):
        self.assertEqual(static_opt([1,1],[5,4,3,2,1])[0], [1,5,4,3,2])
        self.assertEqual(static_opt([1,1],[5,4,3,2,1])[1], 4+1+1)  # switch cost + access cost + access cost
        self.assertEqual(static_opt([1,1],[5,4,3,2,1])[2], [4, 5, 6])


if __name__== "__main__":
    unittest.main()
