import random
import copy
import MTF
import decreasingFreqList
import Transpose
from multiprocessing.pool import ThreadPool
import sys


def main():
    try:
        # Python 2
        xrange
    except NameError:
        # Python 3, xrange is now named range
        xrange = range

    # Increase the size of the list to yield a better result (e.g. set size to 300), but it will take longer to run
    K = 200
    N = 10000
    theList = random.sample(xrange(10000),K)
    # print(theList)
    sequence = []

    # adversary sequence

    # sequence = theList[::-1]
    # for i in range(2000):
    #     sequence.extend(theList[::-1])


    # uniform random sequence
    sequence = generateUniformDistributionSequence(theList, N, K)

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

    print('mtf cost: {0}'.format(mtf_cost))
    print('transpose cost: {0}'.format(transpose_cost))
    print('fc cost: {0}'.format(fc_cost))

    print('cost ratio between MTF and FC is {0}'.format(float(mtf_cost)/ float(fc_cost)))

    print('cost ratio between Transpose and FC is {0}'.format(float(mtf_cost)/ float(transpose_cost)))


def generateUniformDistributionSequence(theList, N, K):
    sequence = []
    for i in range(N):
        sequence.append(theList[random.randint(0,K-1)])
    return sequence


if __name__== "__main__":
    main()
