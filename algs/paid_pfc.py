long_name = "Paid Positional Frequency Count"
short_name = "ppfc"

def serve_accesses(sequence, working_list):
    total_cost = 0
    cost_counters = [0] * len(working_list)
    for s in sequence:
        index = working_list.index(s)
        total_cost += index + 1
        cost_counters[index] += index+1

        while index>0 and cost_counters[index] > cost_counters[index-1]:
            working_list[index], working_list[index-1] = working_list[index-1], working_list[index]
            cost_counters[index], cost_counters[index-1] = cost_counters[index-1], cost_counters[index]
            index -= 1
            total_cost += 1

    return working_list, total_cost
