import unittest
import copy


def accessTimestamp(sequence = [], inputList = []):
    outputList = copy.deepcopy(inputList)

    # TODO

    return outputList





def extractTimestampWindows(sequence = [], accessIndex = 0):
    timestampWindow = []
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
        self.assertEqual(extractTimestampWindows([1,2,3,4,5], 4), [])

    def test_timestamp_windows_2(self):
        self.assertEqual(extractTimestampWindows([5,2,3,4,5], 4), [2,3,4])

    def test_timestamp_windows_3(self):
        self.assertEqual(extractTimestampWindows([1,2,4,4,5], 3), [])

    def test_timestamp_windows_4(self):
        self.assertEqual(extractTimestampWindows([1,4,2,4,5], 3), [2])



if __name__== "__main__":
    unittest.main()