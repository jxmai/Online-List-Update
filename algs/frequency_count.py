import unittest
from collections import Counter

long_name = "Frequency Count"
short_name = "fc"

# Assume no free exchanges, and ignore the initial rearrange cost
def serve_accesses(sequence, working_list):
    cnt = Counter()

    # initialize counter
    for o in working_list:
        if o not in cnt:
            cnt[o] = 0

    total_cost = 0
    total_cost_tracker = []

    for s in sequence:
        for i in range(len(working_list)):
            if working_list[i] == s:
                popped = working_list.pop(i)
                # access cost
                total_cost += i + 1

                cnt[popped] += 1
                previous_index = i - 1

                inserted = False
                while previous_index >= 0:
                    if cnt[working_list[previous_index]] >= cnt[popped]:
                        working_list.insert(previous_index + 1, popped)
                        inserted = True
                        break
                    previous_index = previous_index - 1
                if not inserted:
                    working_list.insert(0, popped)
                    total_cost += i
                else:
                    total_cost += i - previous_index - 1

                total_cost_tracker.append(total_cost)

    return working_list, total_cost, total_cost_tracker


class TestDFC(unittest.TestCase):
    def test_DFC_1(self):
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[0], [1, 5, 4, 3, 2])
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[1], 9)
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[2], [9])

    def test_DFC_2(self):
        self.assertEqual(serve_accesses([1, 2], [5, 4, 3, 2, 1])[0], [1, 2, 5, 4, 3])
        self.assertEqual(serve_accesses([1, 2], [5, 4, 3, 2, 1])[1], 9 + 8)
        self.assertEqual(serve_accesses([1, 2], [5, 4, 3, 2, 1])[2], [9, 17])

    def test_DFC_3(self):
        self.assertEqual(serve_accesses([1, 2, 2], [5, 4, 3, 2, 1])[0], [2, 1, 5, 4, 3])
        self.assertEqual(serve_accesses([1, 2, 2], [5, 4, 3, 2, 1])[1], 9 + 8 + 3)
        self.assertEqual(serve_accesses([1, 2, 2], [5, 4, 3, 2, 1])[2], [9, 17, 20])

    def test_DFC_4(self):
        self.assertEqual(serve_accesses([1, 2, 2, 5], [5, 4, 3, 2, 1])[0], [2, 1, 5, 4, 3])
        self.assertEqual(serve_accesses([1, 2, 2, 5], [5, 4, 3, 2, 1])[1], 9 + 8 + 3 + 3)
        self.assertEqual(serve_accesses([1, 2, 2, 5], [5, 4, 3, 2, 1])[2], [9, 17, 20, 23])

    def test_DFC_5(self):
        self.assertEqual(serve_accesses([1, 2, 2, 5, 5], [5, 4, 3, 2, 1])[0], [2, 5, 1, 4, 3])
        self.assertEqual(serve_accesses([1, 2, 2, 5, 5], [5, 4, 3, 2, 1])[1], 9 + 8 + 3 + 3 + 4)
        self.assertEqual(serve_accesses([1, 2, 2, 5, 5], [5, 4, 3, 2, 1])[2], [9, 17, 20, 23, 27])

    def test_DFC_6(self):
        self.assertEqual(serve_accesses([1, 2, 2, 5, 5, 3, 3, 3, 3], [5, 4, 3, 2, 1])[0], [3, 2, 5, 1, 4])
        self.assertEqual(serve_accesses([1, 2, 2, 5, 5, 3, 3, 3, 3], [5, 4, 3, 2, 1])[1],
                         9 + 8 + 3 + 3 + 4 + 6 + 5 + 5 + 1)
        self.assertEqual(serve_accesses([1, 2, 2, 5, 5, 3, 3, 3, 3], [5, 4, 3, 2, 1])[2],
                         [9, 17, 20, 23, 27, 33, 38, 43, 44])


if __name__ == "__main__":
    unittest.main()
