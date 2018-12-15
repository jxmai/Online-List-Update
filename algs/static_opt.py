import collections as c
import unittest

long_name = "Static OPT"
short_name = "static opt"

# Assume no free exchanges
def serve_accesses(sequence, working_list):
    total_cost = 0
    total_cost_tracker = []
    counts = c.Counter(sequence)

    insert_index = 0
    # order by frequency
    for i in counts.most_common():
        item_index = working_list.index(i[0])  # i = (item, frequency)
        # number of switches
        assert item_index >= insert_index
        total_cost += item_index - insert_index
        working_list.insert(insert_index, working_list.pop(item_index))
        insert_index += 1

    total_cost_tracker.append(total_cost)
    # check if ordered correctly
    # assert working_list == [i[0] for i in counts.most_common()]

    for s in sequence:
        total_cost += working_list.index(s) + 1
        total_cost_tracker.append(total_cost)

    return working_list, total_cost, total_cost_tracker


class StaticOPTTest(unittest.TestCase):

    def test_Static_OPT_1(self):
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[0], [1, 5, 4, 3, 2])
        self.assertEqual(serve_accesses([1], [5, 4, 3, 2, 1])[1], 5)

    def test_Static_OPT_2(self):
        self.assertEqual(serve_accesses([1, 1], [5, 4, 3, 2, 1])[0], [1, 5, 4, 3, 2])
        self.assertEqual(serve_accesses([1, 1], [5, 4, 3, 2, 1])[1],
                         4 + 1 + 1)  # switch cost + access cost + access cost
        self.assertEqual(serve_accesses([1, 1], [5, 4, 3, 2, 1])[2], [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
