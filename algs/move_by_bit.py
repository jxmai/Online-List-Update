import unittest


# Assume no free exchanges
def serve_accesses(sequence, working_list):
    total_cost = 0
    total_cost_tracker = []
    bit_list = [0] * len(working_list)
    for s in sequence:
        item_index = working_list.index(s)
        if bit_list[item_index] == 0:
            bit_list[item_index] = 1
            total_cost += item_index + 1
        else:
            bit_list[item_index] = 0
            total_cost += (2 * item_index) + 1
            working_list.insert(0, working_list.pop(item_index))
            bit_list.insert(0, bit_list.pop(item_index))
        total_cost_tracker.append(total_cost)
    return working_list, total_cost, total_cost_tracker


class MoveByBitTest(unittest.TestCase):

    def test_MTF_1(self):
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[0], [5, 4, 3, 2, 1])
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[1], 5)

    def test_MTF_2(self):
        self.assertEqual(serve_accesses([1, 1], [5, 4, 3, 2, 1])[0], [1, 5, 4, 3, 2])
        self.assertEqual(serve_accesses([1, 1], [5, 4, 3, 2, 1])[1],
                         5 + 5 + 4)  # access cost + access cost + switch cost
        self.assertEqual(serve_accesses([1, 1], [5, 4, 3, 2, 1])[2], [5, 14])


if __name__ == "__main__":
    unittest.main()
