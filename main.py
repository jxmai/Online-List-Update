import math
import os
import random
import re
from multiprocessing.pool import ThreadPool

import matplotlib.pyplot as plt
import numpy as np
# Different list algorithms
from algs import move_to_front, frequency_count, move_by_bit, static_opt, timestamp, transpose, opt


def main():
    list_alg = [move_to_front, frequency_count, transpose,
                timestamp, move_by_bit, static_opt, opt]
    name_alg = [a.__name__[5:] for a in list_alg]
    name_alg[-1] = "approx_off"
    short_names = ['mtf', 'fc', 'trans', 'ts', 'mbb', 'approx_off']
    # remove the name opt as we don't want that on plot
    name_alg.pop(list_alg.index(static_opt))

    analyze_worst_case(10, 3000)
    analyze_dist(list_alg, name_alg, short_names)
    analyze_context(list_alg, name_alg, short_names)

    plt.show()


def analyze_worst_case(K, N):

    # populate initial random list
    initial_list = [i for i in range(K)]
    list_alg = [move_to_front, frequency_count, transpose, timestamp, move_by_bit]
    name_alg = [a.__name__[5:] for a in list_alg]
    short_names = ['mtf', 'fc', 'trans', 'ts', 'mbb']

    mtf_ts = initial_list[::-1]
    trans = [initial_list[-1], initial_list[-2]]
    mbb = initial_list[:]
    for i in initial_list:
        mbb.append(i)
        mbb.append(i)
        mbb.append(i)
    mbb.extend(initial_list[::-1])
    for i in initial_list[::-1]:
        mbb.append(i)
        mbb.append(i)
        mbb.append(i)
    fc = []
    for i in initial_list:
        fc.extend([i]*10)

    sequences = [mtf_ts, fc, trans, mtf_ts, mbb]
    cr = []

    print()
    print("Worst Case")

    for i, a in enumerate(list_alg):
        cost_alg = {a: [], opt: [], static_opt: []}
        seq = replicate_seq(sequences[i], K, N)
        # move by bit requires initial setup before repeating sequence
        if a is move_by_bit:
            seq = initial_list + seq
            seq = seq[:N]
        simulate_seq(initial_list, seq, [opt, a], cost_alg)
        print(a.__name__[5:], cost_alg[a][0] - N, cost_alg[opt][0] - N)
        cr.append((cost_alg[a][0] - N)/(cost_alg[opt][0] - N))
    short_names = ['dcba', 'a^10b^10c^10d^10', 'dc', 'dcba', 'abaaabbbbabbbaaa']
    plot_data(["Worst cases"], name_alg, short_names, cr, False, 'Worst-case cost ratio',
              'Worst-cases compared to approx off')


def replicate_seq(seq, K, N):
    # print(K, N, math.ceil(N/float(len(seq))))
    c_seq = seq * math.ceil(N/float(len(seq)))
    return c_seq[:N]


def analyze_dist(list_alg, name_alg, short_names):
    # Increase the size of the list to yield a better result
    # (e.g. set size to 300), but it will take longer to run
    # K = 50
    # N = 1000  # 10000

    K = 500
    N = 10000

    # populate initial random list
    initial_list = [i for i in range(K)]
    random.shuffle(initial_list)

    dist = ['Uniform dist', 'Normal dist', 'Logistic dist', 'Zipf dist']
    sequences = [gen_uni_dist(N, K), gen_normal_dist(
        N, K), gen_logistic_dist(N, K), gen_zipf_dist(initial_list, N, K)]
    cost_alg = {a: [] for a in list_alg}

    for d in sequences:
        simulate_seq(initial_list, d, list_alg, cost_alg)

    print()
    print("Distribution")
    for a in list_alg:
        print(a.__name__[5:], cost_alg[a])

    # find competitive ratio for all the algorithms except static opt
    cr = find_cr(list_alg, len(dist), cost_alg)
    # plot the results
    plot_data(dist, name_alg, short_names, cr, True, 'Average cost ratio',
              'Average cost ratio on distributions compared to static opt')


def analyze_context(list_alg, name_alg, short_names):
    # files = ["alice29.txt", "pi.txt"]#, "bible.txt"]
    files = ["alice29.txt", "pi.txt", "bible.txt"]
    cost_alg = {a: [] for a in list_alg}

    for file in files:
        initial_list, sequence = gen_seq_file(os.path.join("datasets", file))
        simulate_seq(initial_list, sequence, list_alg, cost_alg)

    print()
    print("Context")
    for a in list_alg:
        print(a.__name__[5:], cost_alg[a])
    # find competitive ratio for all the algorithms except static opt
    cr = find_cr(list_alg, len(files), cost_alg)
    # plot the results

    plot_data(files, name_alg, short_names, cr, True, 'Average cost ratio',
              'Average cost ratio on data sets with context compared to static opt')


def plot_data(x_labels, name_alg, short_names, cr, limit, ylabel, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # necessary variables
    ind = np.arange(len(x_labels))  # the x locations for the groups
    width = 0.12  # the width of the bars
    rects = None
    for i, a in enumerate(cr):
        if rects == None:
            rects = ax.bar(ind + (width * i), a, width)
        else:
            rects += ax.bar(ind + (width * i), a, width)
        # Add counts above the two bar graphs

    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height,
                 '%0.2f' % (height), ha='center', va='bottom')

    i = 0
    j = 0
    for rect in rects:
        if i == len(x_labels):
            i = 0
            j += 1
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height/1.3,
                 '%s' % short_names[j], ha='center', va='top')
        i += 1

    # axes and labels
    if limit:
        ax.set_ylim(0.5, 3)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(ind + width)
    plt.setp(ax.set_xticklabels(x_labels), fontsize=10)
    ax.legend(name_alg)
    # plt.show()


def simulate_seq(initial_list, sequence, list_alg, cost_alg):
    # Create a pool of number of algorithms worker threads
    pool = ThreadPool(processes=len(list_alg))
    for a in list_alg:
        # simulate an algorithm on a thread
        cost = pool.apply_async(
            a.serve_accesses, (sequence, initial_list[:])).get()
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
