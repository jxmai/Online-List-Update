import os
import random
import numpy as np
import matplotlib.pyplot as plt

from seq_helper import *
# Different list algorithms
from algs import move_to_front, frequency_count, move_by_bit, static_opt, timestamp, transpose, approx_off, paid_pfc


def main():
    list_alg = [paid_pfc, move_to_front, frequency_count, transpose,
                timestamp, move_by_bit, static_opt, approx_off]

    # analyze_dist(list_alg)
    # analyze_context(list_alg)
    # analyze_worst_case(10, 3000)
    analyze_ppfc(500, 50000)
    # analyze_ppfc(1000, 30000)
    # analyze_ppfc_static(500, 50000)
    plt.show()


def analyze_ppfc(K, N):
    # populate initial random list
    initial_list = [i for i in range(K)]
    # list_alg = [paid_pfc, paid_pfc, paid_pfc, paid_pfc, paid_pfc]
    list_alg = [paid_pfc]

    paid = initial_list[::-1]
    paid.extend(initial_list)

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
        fc.extend([i]*100)

    # sequences = [paid, mtf_ts, fc, trans, mbb]
    sequences = [fc]
    cr = []

    print()
    print("Worst Case")
    for i, a in enumerate(list_alg):
        cost_alg = {a: [], approx_off: [], static_opt: []}
        seq = replicate_seq(sequences[i], K, N)
        # move by bit requires initial setup before repeating sequence
        if a is move_by_bit:
            seq = initial_list + seq
            seq = seq[:N]
        simulate_seq(initial_list, seq, [approx_off, a], cost_alg)
        print(a.__name__[5:], cost_alg[a][0], cost_alg[approx_off][0])
        cr.append((cost_alg[a][0])/(cost_alg[approx_off][0]))
    short_names = ['dcbaabcd', 'dcba', 'a^10b^10c^10d^10', 'dc', 'abaaabbbbabbbaaa']
    name_alg = get_names(list_alg)
    name_alg = [(name_alg[i][0], short_names[i]) for i in range(len(name_alg))]
    plot_data(["Worst cases"], name_alg, cr, False, 'Worst-case cost ratio',
              'Worst-cases compared to approx off')


def analyze_ppfc_static(K, N):
    # populate initial random list
    initial_list = [i for i in range(K)]
    list_alg = [paid_pfc, paid_pfc, paid_pfc, paid_pfc, paid_pfc]

    paid = initial_list[::-1]
    paid.extend(initial_list)

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
        fc.extend([i]*100)

    sequences = [paid, mtf_ts, fc, trans, mbb]
    cr = []

    print()
    print("Worst Case")
    for i, a in enumerate(list_alg):
        cost_alg = {a: [], static_opt: []}
        seq = replicate_seq(sequences[i], K, N)
        # move by bit requires initial setup before repeating sequence
        if a is move_by_bit:
            seq = initial_list + seq
            seq = seq[:N]
        simulate_seq(initial_list, seq, [static_opt, a], cost_alg)
        print(a.__name__[5:], cost_alg[a][0], cost_alg[static_opt][0])
        cr.append((cost_alg[a][0])/(cost_alg[static_opt][0]))
    short_names = ['dcbaabcd', 'dcba', 'a^10b^10c^10d^10', 'dc', 'abaaabbbbabbbaaa']
    name_alg = get_names(list_alg)
    name_alg = [(name_alg[i][0], short_names[i]) for i in range(len(name_alg))]
    plot_data(["Worst cases"], name_alg, cr, False, 'Worst-case cost ratio',
              'Worst-cases compared to static opt')


def get_names(list_alg):
    name_alg = []
    for a in list_alg:
        if a is not static_opt:
            name_alg.append((a.long_name, a.short_name))
    return name_alg


def analyze_worst_case(K, N):
    # populate initial random list
    initial_list = [i for i in range(K)]
    list_alg = [move_to_front, frequency_count, transpose, timestamp, move_by_bit]

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
        cost_alg = {a: [], approx_off: [], static_opt: []}
        seq = replicate_seq(sequences[i], K, N)
        # move by bit requires initial setup before repeating sequence
        if a is move_by_bit:
            seq = initial_list + seq
            seq = seq[:N]
        simulate_seq(initial_list, seq, [approx_off, a], cost_alg)
        print(a.__name__[5:], cost_alg[a][0] - N, cost_alg[approx_off][0] - N)
        cr.append((cost_alg[a][0] - N)/(cost_alg[approx_off][0] - N))
    short_names = ['dcba', 'a^10b^10c^10d^10', 'dc', 'dcba', 'abaaabbbbabbbaaa']
    name_alg = get_names(list_alg)
    name_alg = [(name_alg[i][0], short_names[i]) for i in range(len(name_alg))]
    plot_data(["Worst cases"], name_alg, cr, False, 'Worst-case cost ratio',
              'Worst-cases compared to approx off')


def analyze_dist(list_alg):
    K = 500  # number of items
    N = 10000    # length of sequence

    # populate initial random list
    initial_list = [i for i in range(K)]
    random.shuffle(initial_list)

    dist = ['Uniform dist', 'Normal dist', 'Logistic dist', 'Zipf dist']
    sequences = [gen_uni_dist(N, K), gen_normal_dist(N, K), 
                gen_logistic_dist(N, K), gen_zipf_dist(initial_list, N, K)]
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
    plot_data(dist, get_names(list_alg), cr, True, 'Average cost ratio',
              'Average cost ratio on distributions compared to static opt')


def analyze_context(list_alg):
    # files = ["alice29.txt", "pi.txt"]#, "bible.txt"]
    files = ["alice29.txt"]#, "pi.txt"]
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
    plot_data(files, get_names(list_alg), cr, True, 'Average cost ratio',
              'Average cost ratio on data sets with context compared to static opt')


def plot_data(x_labels, name_alg, cr, limit, ylabel, title):
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
                 '%s' % name_alg[j][1], ha='center', va='top')
        i += 1

    # axes and labels
    if limit:
        ax.set_ylim(0.5, 3)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(ind + width)
    plt.setp(ax.set_xticklabels(x_labels), fontsize=10)
    ax.legend([x[0] for x in name_alg])


def find_cr(list_alg, N, cost_alg):
    cr = []
    for a in list_alg:
        cr.append([])
        for i in range(N):
            cr[-1].append(float(cost_alg[a][i]) / cost_alg[static_opt][i])
    # remove the competitive ratio of opt as it would be 1
    cr.pop(list_alg.index(static_opt))
    return cr

if __name__ == "__main__":
    main()
