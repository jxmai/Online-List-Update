long_name = "Approximate Offline"
short_name = "approx off"

def static_state(current_list, future_sequence):
    data = {}
    # can improve this
    for i in current_list:
        data[i] = [0, []]
    for i,s in enumerate(future_sequence):
        # increment counter and add position
        data[s][0] += 1
        data[s][1].append(i)
    return data


def maintain(current_list, state):
    _cost = 0
    # go through list and maintain
    i = 0
    while i+1 < len(current_list):
        i = 1 if i < 1 else i + 1

        x, y = current_list[i - 1], current_list[i]

        # check if x and y needs to be switched
        if state[y][0] < 2:
            continue

        if state[x][0] < 1:
            current_list[i - 1], current_list[i] = y, x
            _cost += 1
            # go back as this item might move more
            i -= 2
            # print("switched")
        else:
            first_x = state[x][1][0]
            first_y = state[y][1][0]
            # next symbol is y
            if first_y < first_x:
                second_y = state[y][1][1]
                # symbol after y is also y
                if second_y < first_x:
                    current_list[i - 1], current_list[i] = y, x
                    _cost += 1
                    i -= 2
                    # print("switched")
    return _cost


def serve_accesses(sequence, current_list):
    cost = 0
    state = static_state(current_list, sequence)
    for s in range(len(sequence)):
        # paid exchanges to maintain OPT
        cost += maintain(current_list, state)
        # serve request
        cost += current_list.index(sequence[s]) + 1
        # decrement count
        state[sequence[s]][0] -= 1
        # remove position
        state[sequence[s]][1].pop(0)
    return [current_list, cost, []]
