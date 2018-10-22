import random
import unittest
import copy
import MTF



def main():
    theList = random.sample(xrange(10000),10)
    # print(theList)
    sequence = []

    # adversary sequence
    sequence = theList[::-1]
    # print(sequence)

    #random sequence (hide for now)
    # for i in range(100):
    #     sequence.append(theList[random.randint(0,len(theList)-1)])
    # print sequence
    cost = (MTF.moveToFront(sequence, theList))[1]
    print(cost)


if __name__== "__main__":
    main()
