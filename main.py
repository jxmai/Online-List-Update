import os
import random
import re
from multiprocessing.pool import ThreadPool

import matplotlib.pyplot as plt
import numpy as np

# Different list algorithms
from algs import move_to_front, frequency_count, move_by_bit, static_opt, timestamp, transpose


def main():
    # Increase the size of the list to yield a better result (e.g. set size to 300), but it will take longer to run
    K = 50
    N = 1000  # 10000

    # populate initial random list
    initial_list = [i for i in range(K)]
    random.shuffle(initial_list)

    # adversary sequence
    # sequence = initial_list[::-1]
    # for i in range(2000):
    #     sequence.extend(initial_list[::-1])
    # print(sequence)

    cost_analysis(initial_list, gen_uni_dist(N, K), 'Uniform distribution')
    cost_analysis(initial_list, gen_normal_dist(N, K), 'Normal distribution')
    cost_analysis(initial_list, gen_logistic_dist(N, K), 'Logistic distribution')
    cost_analysis(initial_list, gen_zipf_dist(initial_list, N, K), 'Zipf distribution')

    files = ["alice29.txt", "pi.txt"]  # "bible.txt
    for file in files:
        initial_list, sequence = gen_seq_file(os.path.join("datasets", file))
        cost_analysis(initial_list, sequence, "\n\nData from " + file)


def cost_analysis(initial_list, sequence, description):

    print(description)

    list_alg = [move_to_front, frequency_count, transpose, timestamp, move_by_bit, static_opt]

    # Create a pool of number of algorithms worker threads
    pool = ThreadPool(processes=len(list_alg))

    results = {alg: pool.apply_async(alg.serve_accesses, (sequence, initial_list[:])) for alg in list_alg}

    pool.close()
    pool.join()

    print("\nCost of algorithms:")
    for a in list_alg:
        print("Cost of {0} is {1}".format(a.__name__[5:], results[a].get()[1]))

    print("\nCost of algorithms relative to static_opt:")
    for a in list_alg:
        if a is not static_opt:
            print(
                "Cost of {0} is {1}".format(a.__name__[5:], float(results[a].get()[1]) / results[static_opt].get()[1]))

    # draw plot for current graph
    plt.figure(num=description)
    plt.xlabel("Sequence length")
    plt.ylabel("Total cost")
    for a in list_alg:
        if a is not static_opt:
            plt.plot(range(len(sequence)), results[a].get()[2], label=a.__name__[5:])
        else:  # static opt requires plus 1 as it does is initial placing
            plt.plot(range(len(sequence) + 1), results[a].get()[2], label=a.__name__[5:])
    plt.legend()
    plt.show()


def gen_uni_dist(N, K):
    return list(np.random.randint(0, K, N))


def gen_normal_dist(N, K):
    dist = np.random.normal(K / 2, K / 4, N)
    dist = list(dist)
    for i in range(len(dist)):
        dist[i] = max(0, round(dist[i]))
        dist[i] = min(round(dist[i]), K - 1)
    return dist


def gen_logistic_dist(N, K):
    dist = np.random.logistic(K / 2, K / 4, N)
    dist = list(dist)
    for i in range(len(dist)):
        dist[i] = max(0, round(dist[i]))
        dist[i] = min(round(dist[i]), K - 1)
    return dist


def gen_zipf_dist(initial_list, N, K):
    a = 2   # parameter
    indexes = np.random.zipf(a, N)
    indexes = list(map(lambda x: K-1 if x >= K else x, indexes))
    sequence = list(map(lambda x: initial_list[x], indexes))
    return sequence


def gen_seq_file(file_name):
    f = open(file_name, 'r')
    text = f.read()
    # remove all the whitespace
    text = re.sub(r"\s", "", text).lower()
    # find all the unique letters
    unique_letters = list(set(text))
    # map all unique letters to a unique number
    all_mappings = {unique_letters[i]: i for i in range(len(unique_letters))}
    # map all letters to there symbols
    sequence = [all_mappings[l] for l in text]

    # create initial list depending on the number of unique letters
    initial_list = [i for i in range(len(unique_letters))]
    random.shuffle(initial_list)

    return initial_list, sequence


if __name__ == "__main__":
    main()
