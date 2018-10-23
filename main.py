import random
import unittest
import copy
import MTF
import decreasingFreqList
import Transpose
from multiprocessing.pool import ThreadPool
import sys
from fractions import Fraction


def main():
    # Increase the size of the list to yield a better result (e.g. set size to 300), but it will take longer to run
    theList = random.sample(xrange(10000),100)
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

    pool = ThreadPool(processes=3)


    mtf_result = pool.apply_async(MTF.moveToFront, (sequence, theList))
    fc_result = pool.apply_async(decreasingFreqList.accessDecreasingFreqList, (sequence, theList))
    transpose_result = pool.apply_async(Transpose.accessTranspose, (sequence, theList))

    pool.close()
    pool.join()  
    
    mtf_cost = mtf_result.get()[1]
    fc_cost = fc_result.get()[1]
    transpose_cost = transpose_result.get()[1]

    print('competitive ratio between MTF and FC is {0}'.format(float(mtf_cost)/ float(fc_cost)))

    print('competitive ratio between Transpose and FC is {0}'.format(float(mtf_cost)/ float(transpose_cost)))

if __name__== "__main__":
    main()
