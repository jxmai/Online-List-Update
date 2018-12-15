import unittest

long_name = "Timestamp"
short_name = "ts"

def serve_accesses(sequence, working_list):
    total_cost = 0
    total_cost_tracker = []

    for seqIndex in range(len(sequence)):
        for i in range(len(working_list)):
            if working_list[i] == sequence[seqIndex]:
                # access cost
                total_cost += i + 1
                timestamp_window = extract_timestamp_window(sequence, seqIndex)

                if timestamp_window is not None:
                    for j in range (0,i):
                        if timestamp_window.count(working_list[j]) <= 1:
                            popped = working_list.pop(i)
                            working_list.insert(j, popped)
                            total_cost += i - j
                            break
                total_cost_tracker.append(total_cost)

    return working_list, total_cost, total_cost_tracker


def extract_timestamp_window(sequence, access_index):
    timestamp_window = None

    curr_index = access_index - 1

    while curr_index >= 0:
        if sequence[curr_index] == sequence[access_index]:
            timestamp_window = sequence[curr_index + 1: access_index]
            break
        curr_index -= 1
    return timestamp_window


class TimestampTest(unittest.TestCase):
    def test_timestamp_windows_1(self):
        self.assertEqual(extract_timestamp_window([1, 2, 3, 4, 5], 4), None)

    def test_timestamp_windows_2(self):
        self.assertEqual(extract_timestamp_window([5, 2, 3, 4, 5], 4), [2, 3, 4])

    def test_timestamp_windows_3(self):
        self.assertEqual(extract_timestamp_window([1, 2, 4, 4, 5], 3), [])

    def test_timestamp_windows_4(self):
        self.assertEqual(extract_timestamp_window([1, 4, 2, 4, 5], 3), [2])

    def test_timestamp_access_1(self):
        self.assertEqual(serve_accesses([5], [1, 2, 3, 4, 5])[0], [1, 2, 3, 4, 5])
        self.assertEqual(serve_accesses([5], [1, 2, 3, 4, 5])[1], 5)
        self.assertEqual(serve_accesses([5], [1, 2, 3, 4, 5])[2], [5])

    def test_timestamp_access_2(self):
        self.assertEqual(serve_accesses([5, 5], [1, 2, 3, 4, 5])[0], [5, 1, 2, 3, 4])
        self.assertEqual(serve_accesses([5, 5], [1, 2, 3, 4, 5])[1], 5 + 9)
        self.assertEqual(serve_accesses([5, 5], [1, 2, 3, 4, 5])[2], [5, 14])

    def test_timestamp_access_3(self):
        self.assertEqual(serve_accesses([5, 1, 1, 5], [1, 2, 3, 4, 5])[0], [1, 5, 2, 3, 4])
        self.assertEqual(serve_accesses([5, 1, 1, 5], [1, 2, 3, 4, 5])[1], 5 + 1 + 1 + 8)
        self.assertEqual(serve_accesses([5, 1, 1, 5], [1, 2, 3, 4, 5])[2], [5, 6, 7, 15])


if __name__ == "__main__":
    unittest.main()
