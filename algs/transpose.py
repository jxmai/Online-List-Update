import unittest

long_name = "Transpose"
short_name = "trans"

def serve_accesses(sequence, working_list):
    total_cost = 0
    total_cost_tracker = []

    for s in sequence:
        for i in range(len(working_list)):
            if working_list[i] == s:
                total_cost += i + 1
                if i != 0:
                    working_list.insert(i - 1, working_list.pop(i))
                    total_cost += 1
                total_cost_tracker.append(total_cost)

    return working_list, total_cost, total_cost_tracker


class TransposeTest(unittest.TestCase):
    def test_transpose_1(self):
        self.assertEqual(serve_accesses([5], [1, 2, 3, 4, 5])[0], [1, 2, 3, 5, 4])
        self.assertEqual(serve_accesses([5], [1, 2, 3, 4, 5])[1], 6)
        self.assertEqual(serve_accesses([5], [1, 2, 3, 4, 5])[2], [6])

    def test_transpose_2(self):
        self.assertEqual(serve_accesses([5, 5], [1, 2, 3, 4, 5])[0], [1, 2, 5, 3, 4])
        self.assertEqual(serve_accesses([5, 5], [1, 2, 3, 4, 5])[1], 6 + 5)
        self.assertEqual(serve_accesses([5, 5], [1, 2, 3, 4, 5])[2], [6, 11])

    def test_transpose_3(self):
        self.assertEqual(serve_accesses([5, 5, 2], [1, 2, 3, 4, 5])[0], [2, 1, 5, 3, 4])
        self.assertEqual(serve_accesses([5, 5, 2], [1, 2, 3, 4, 5])[1], 6 + 5 + 3)
        self.assertEqual(serve_accesses([5, 5, 2], [1, 2, 3, 4, 5])[2], [6, 11, 14])

    def test_transpose_4(self):
        self.assertEqual(serve_accesses([5, 5, 2, 2], [1, 2, 3, 4, 5])[0], [2, 1, 5, 3, 4])
        self.assertEqual(serve_accesses([5, 5, 2, 2], [1, 2, 3, 4, 5])[1], 6 + 5 + 3 + 1)
        self.assertEqual(serve_accesses([5, 5, 2, 2], [1, 2, 3, 4, 5])[2], [6, 11, 14, 15])


if __name__ == "__main__":
    unittest.main()
