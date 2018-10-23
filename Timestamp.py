import unittest
import copy


def accessTimestamp(sequence = [], inputList = []):
    outputList = copy.deepcopy(inputList)

    # TOOD finish the cost calculation later
    totalCost = 0
    for seqIndex in range(len(sequence)):
        for i in range(len(outputList)):
            if outputList[i] == outputList[seqIndex]:
                # access cost
                totalCost += i + 1
                timestampWindow = extractTimestampWindows(sequence, seqIndex)

                if timestampWindow is not None:
                    for j in range (0,i):
                        if timestampWindow.count(outputList[j]) <= 1:
                            popped = outputList.pop(i)
                            outputList.insert(j, popped)
                            break

    return outputList


def extractTimestampWindows(sequence = [], accessIndex = 0):
    timestampWindow = None
    foundPreviousAccess = False

    currIndex = accessIndex - 1

    while currIndex >= 0:
        if sequence[currIndex] == sequence[accessIndex]:
            foundPreviousAccess = True
            timestampWindow = sequence[currIndex + 1 : accessIndex]
            break
        currIndex -= 1
    return timestampWindow

class TestTimestamp(unittest.TestCase):
    def test_timestamp_windows_1(self):
        self.assertEqual(extractTimestampWindows([1,2,3,4,5], 4), None)

    def test_timestamp_windows_2(self):
        self.assertEqual(extractTimestampWindows([5,2,3,4,5], 4), [2,3,4])

    def test_timestamp_windows_3(self):
        self.assertEqual(extractTimestampWindows([1,2,4,4,5], 3), [])

    def test_timestamp_windows_4(self):
        self.assertEqual(extractTimestampWindows([1,4,2,4,5], 3), [2])

    def test_timestamp_access_1(self):
        self.assertEqual(accessTimestamp([5], [1,2,3,4,5]), [1,2,3,4,5])

    def test_timestamp_access_2(self):
        self.assertEqual(accessTimestamp([5,5], [1,2,3,4,5]), [5,1,2,3,4])



if __name__== "__main__":
    unittest.main()