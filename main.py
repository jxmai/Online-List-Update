import random
import copy
import MTF
import decreasingFreqList
import Transpose
import Timestamp
from multiprocessing.pool import ThreadPool
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


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

    # adversary sequence
    # sequence = theList[::-1]
    # for i in range(2000):
    #     sequence.extend(theList[::-1])

    # print(sequence)

    costAnalysis(theList, generateZipfDistribtion(theList, N, K), 'zipf distribution random sequence')

    costAnalysis(theList, generateUniformDistributionSequence(theList, N, K), 'uniform distribution random sequence')



def costAnalysis(theList = [], sequence = [], description = ''):

    print(description)

    pool = ThreadPool(processes=4)

    mtf_result = pool.apply_async(MTF.moveToFront, (sequence, theList))
    fc_result = pool.apply_async(decreasingFreqList.accessDecreasingFreqList, (sequence, theList))
    transpose_result = pool.apply_async(Transpose.accessTranspose, (sequence, theList))
    timestamp_result = pool.apply_async(Timestamp.accessTimestamp, (sequence, theList))

    pool.close()
    pool.join()  
    
    mtf_cost = mtf_result.get()[1]
    fc_cost = fc_result.get()[1]
    transpose_cost = transpose_result.get()[1]
    timestamp_cost = timestamp_result.get()[1]

    print('mtf cost: {0}'.format(mtf_cost))


    # visualization needs to be improved further
    plt.plot(range(len(sequence)), mtf_result.get()[2], 'ro')
    plt.plot(range(len(sequence)), fc_result.get()[2], 'bo')
    plt.plot(range(len(sequence)), transpose_result.get()[2], 'go')
    plt.plot(range(len(sequence)), timestamp_result.get()[2], 'yo')
    plt.show()


    print('transpose cost: {0}'.format(transpose_cost))
    print('fc cost: {0}'.format(fc_cost))
    print('timestamp cost: {0}'.format(timestamp_cost))

    print('cost ratio between MTF and FC is {0}'.format(float(mtf_cost)/ float(fc_cost)))

    print('cost ratio between Transpose and FC is {0}'.format(float(transpose_cost)/ float(fc_cost)))

    print('cost ratio between Timestamp and FC is {0}'.format(float(timestamp_cost)/ float(fc_cost)))

    print('')


def generateUniformDistributionSequence(theList, N, K):
    sequence = []
    for i in range(N):
        sequence.append(theList[random.randint(0,K-1)])
    return sequence


def generateZipfDistribtion(theList, N, K):
    sequence = []
    a = 2 # parameter
    indexes = np.random.zipf(a, N)
    indexes = list(map (lambda x: K-1 if x >= K else x, indexes))
    sequence = list(map(lambda x : theList[x], indexes))
    return sequence


if __name__== "__main__":
    main()
