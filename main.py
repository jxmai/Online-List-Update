import os
import random
import re
from multiprocessing.pool import ThreadPool

import matplotlib.pyplot as plt
import numpy as np

# Different list algorithms
from algs import move_to_front, frequency_count, move_by_bit, static_opt, timestamp, transpose


def main():
    list_alg = [move_to_front, frequency_count, transpose, timestamp, move_by_bit, static_opt]
    name_alg = [a.__name__[5:] for a in list_alg]
    # remove the name opt as we don't want that on plot
    name_alg.pop(list_alg.index(static_opt))

    analyze_dist(list_alg, name_alg)
    analyze_context(list_alg, name_alg)


def analyze_dist(list_alg, name_alg):
    # Increase the size of the list to yield a better result
    # (e.g. set size to 300), but it will take longer to run
    K = 50;
    N = 1000  # 10000

    # populate initial random list
    initial_list = [i for i in range(K)]
    random.shuffle(initial_list)

    dist = ['Uniform dist', 'Normal dist', 'Logistic dist', 'Zipf dist']
    sequences = [gen_uni_dist(N, K), gen_normal_dist(N, K), gen_logistic_dist(N, K), gen_zipf_dist(initial_list, N, K)]
    cost_alg = {a: [] for a in list_alg}

    for d in sequences:
        simulate_seq(initial_list, d, list_alg, cost_alg)

    # find competitive ratio for all the algorithms except static opt
    cr = find_cr(list_alg, len(dist), cost_alg)
    # plot the results
    plot_data(dist, name_alg, cr)


def analyze_context(list_alg, name_alg):
    files = ["alice29.txt", "pi.txt"]  # "bible.txt
    cost_alg = {a: [] for a in list_alg}

    for file in files:
        initial_list, sequence = gen_seq_file(os.path.join("datasets", file))
        simulate_seq(initial_list, sequence, list_alg, cost_alg)

    # find competitive ratio for all the algorithms except static opt
    cr = find_cr(list_alg, len(files), cost_alg)
    # plot the results
    plot_data(files, name_alg, cr)


def plot_data(x_labels, name_alg, cr):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # necessary variables
    ind = np.arange(len(x_labels))  # the x locations for the groups
    width = 0.12  # the width of the bars
    for i, a in enumerate(cr):
        ax.bar(ind + (width * i), a, width)

    # axes and labels
    ax.set_ylim(0.5, 3)
    ax.set_ylabel('Average cost ratio')
    ax.set_title('Average cost ratio of List update algorithms')
    ax.set_xticks(ind + width)
    plt.setp(ax.set_xticklabels(x_labels), fontsize=10)
    ax.legend(name_alg)
    plt.show()


def simulate_seq(initial_list, sequence, list_alg, cost_alg):
    # Create a pool of number of algorithms worker threads
    pool = ThreadPool(processes=len(list_alg))
    for a in list_alg:
        # simulate an algorithm on a thread
        cost = pool.apply_async(a.serve_accesses, (sequence, initial_list[:])).get()
        cost_alg[a].append(cost[1])
    pool.close()
    pool.join()


def find_cr(list_alg, N, cost_alg):
    cr = []
    for a in list_alg:
        cr.append([])
        for i in range(N):
            cr[-1].append(float(cost_alg[a][i]) / cost_alg[static_opt][i])
    # remove the competitive ratio of opt as it would be 1
    cr.pop(list_alg.index(static_opt))
    return cr


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
