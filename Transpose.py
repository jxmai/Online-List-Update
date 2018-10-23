import unittest
import copy

# TODO
def accessTranspose(sequence = [], inputList = []):
    return None




class TestTranspose(unittest.TestCase):
    def test_transpose(self):
        self.assertEqual(accessTranspose([5], [1,2,3,4,5]), [1,2,3,5,4])

if __name__== "__main__":
    unittest.main()