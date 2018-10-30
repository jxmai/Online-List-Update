import random
import MTF
import decreasingFreqList
import Transpose
import Timestamp
import Move_by_bit
import Static_opt
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
    # populate initial random list
    theList = [i for i in range(K)]
    random.shuffle(theList)

    # adversary sequence
    # sequence = theList[::-1]
    # for i in range(2000):
    #     sequence.extend(theList[::-1])

    # print(sequence)

    costAnalysis(theList, generateZipfDistribtion(theList, N, K), 'zipf distribution random sequence')

    costAnalysis(theList, generateUniformDistributionSequence(theList, N, K), 'uniform distribution random sequence')



def costAnalysis(theList = [], sequence = [], description = ''):

    print(description)

    pool = ThreadPool(processes=6)

    mtf_result = pool.apply_async(MTF.moveToFront, (sequence, theList))
    fc_result = pool.apply_async(decreasingFreqList.accessDecreasingFreqList, (sequence, theList))
    transpose_result = pool.apply_async(Transpose.accessTranspose, (sequence, theList))
    timestamp_result = pool.apply_async(Timestamp.accessTimestamp, (sequence, theList))
    move_by_bit_result = pool.apply_async(Move_by_bit.move_by_bit, (sequence, theList))
    static_opt_result = pool.apply_async(Static_opt.static_opt, (sequence, theList))

    pool.close()
    pool.join()

    mtf_cost = mtf_result.get()[1]
    fc_cost = fc_result.get()[1]
    transpose_cost = transpose_result.get()[1]
    timestamp_cost = timestamp_result.get()[1]
    move_by_bit_cost = move_by_bit_result.get()[1]
    static_opt_cost = static_opt_result.get()[1]


    print('mtf cost: {0}'.format(mtf_cost))


    # visualization needs to be improved further
    plt.plot(range(len(sequence)), mtf_result.get()[2], label='MTF')
    plt.plot(range(len(sequence)), fc_result.get()[2], label='FC')
    plt.plot(range(len(sequence)), transpose_result.get()[2], label='Transpose')
    plt.plot(range(len(sequence)), timestamp_result.get()[2], label='Timestamp')
    plt.plot(range(len(sequence)), move_by_bit_result.get()[2], label='Move-By-Bit')
    # static opt requires plus 1 as it does is initial placing
    plt.plot(range(len(sequence)+1), static_opt_result.get()[2],label='Static Opt')
    plt.legend()
    plt.show()


    print('transpose cost: {0}'.format(transpose_cost))
    print('fc cost: {0}'.format(fc_cost))
    print('timestamp cost: {0}'.format(timestamp_cost))
    print('move by bit cost: {0}'.format(move_by_bit_cost))
    print('static opt cost: {0}'.format(static_opt_cost))

    print('cost ratio between MTF and FC is {0}'.format(float(mtf_cost)/ float(fc_cost)))
    print('cost ratio between Transpose and FC is {0}'.format(float(transpose_cost)/ float(fc_cost)))
    print('cost ratio between Timestamp and FC is {0}'.format(float(timestamp_cost)/ float(fc_cost)))

    print('\nStatic Opt')
    print('cost ratio MTF {0}'.format(float(mtf_cost)/float(static_opt_cost)))
    print('cost ratio FC {0}'.format(float(fc_cost)/float(static_opt_cost)))
    print('cost ratio Transpose {0}'.format(float(transpose_cost)/float(static_opt_cost)))
    print('cost ratio Timestamp {0}'.format(float(timestamp_cost)/float(static_opt_cost)))
    print('cost ratio Move by bit {0}'.format(float(move_by_bit_cost)/float(static_opt_cost)))
    print()


def generateUniformDistributionSequence(theList, N, K):
    return [random.randrange(K) for i in range(N)]


def generateZipfDistribtion(theList, N, K):
    a = 2   # parameter
    indexes = np.random.zipf(a, N)
    indexes = list(map(lambda x: K-1 if x >= K else x, indexes))
    sequence = list(map(lambda x: theList[x], indexes))
    return sequence


if __name__== "__main__":
    main()
