import copy

# Assume no free exchanges
def move_by_bit(sequence = [], inputList = []):
    totalCost = 0
    outputList = copy.deepcopy(inputList)
    bitList = [0] * len(inputList)
    for s in sequence:
        item_index = outputList.index(s)
        if bitList[item_index] == 0:
            bitList[item_index] = 1
        else:
            bitList[item_index] = 0
            totalCost += (2 * item_index) + 1
            outputList.insert(0, outputList.pop(item_index))
            bitList.insert(0, bitList.pop(item_index))
    return outputList, totalCost

