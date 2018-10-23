import random
import unittest
import copy
import MTF
import decreasingFreqList
from fractions import Fraction


def main():
    theList = random.sample(xrange(10000),300)
    # print(theList)
    sequence = []

    # adversary sequence

    sequence = theList[::-1]
    for i in range(2000):
        sequence.extend(theList[::-1])
    # print(sequence)

    #random sequence (hide for now)
    # for i in range(100):
    #     sequence.append(theList[random.randint(0,len(theList)-1)])
    # print sequence
    mtf_cost = (MTF.moveToFront(sequence, theList))[1]
    fc_cost = (decreasingFreqList.accessDecreasingFreqList(sequence, theList))[1]

    print('competitive ratio between MTF and FC is {0}'.format(float(mtf_cost)/ float(fc_cost)))

if __name__== "__main__":
    main()
