import collections as c

# Assume no free exchanges
def static_opt(sequence = [], inputList = []):
    totalCost = 0
    outputList = inputList[:]
    counts = c.Counter(sequence)

    insert_index = 0
    # order by frequency
    for i in counts.most_common():
        item_index = outputList.index(i[0])     # i = (item, frequency)
        # number of switches
        assert item_index >= insert_index
        totalCost += item_index - insert_index
        outputList.insert(insert_index, outputList.pop(item_index))
        insert_index += 1

    #check if ordered correctly
    #assert outputList == [i[0] for i in counts.most_common()]

    for s in sequence:
        totalCost += outputList.index(s)+1

    return outputList, totalCost

