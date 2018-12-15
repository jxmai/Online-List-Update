import unittest

long_name = "Move to front"
short_name = "mtf"

# Assume no free exchanges
def serve_accesses(sequence, working_list):
    total_cost = 0
    total_cost_tracker = []

    for s in sequence:
        item_index = working_list.index(s)
        total_cost += (2 * item_index) + 1
        total_cost_tracker.append(total_cost)
        working_list.insert(0, working_list.pop(item_index))
    return working_list, total_cost, total_cost_tracker


class MoveToFrontTest(unittest.TestCase):

    def test_MTF_1(self):
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[0], [1, 5, 4, 3, 2])
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[1], 9)
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[2], [9])

    def test_MTF_2(self):
        self.assertEqual(serve_accesses([1, 2], [5, 4, 3, 2, 1])[0], [2, 1, 5, 4, 3])
        self.assertEqual(serve_accesses([1, 2], [5, 4, 3, 2, 1])[1], 18)
        self.assertEqual(serve_accesses([1, 2], [5, 4, 3, 2, 1])[2], [9, 18])


if __name__ == "__main__":
    unittest.main()
