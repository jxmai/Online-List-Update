import re
import math
import random
import numpy as np
from multiprocessing.pool import ThreadPool

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


def replicate_seq(seq, K, N):
    # print(K, N, math.ceil(N/float(len(seq))))
    c_seq = seq * math.ceil(N/float(len(seq)))
    return c_seq[:N]

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
