#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
from matplotlib import pyplot as plt
from tqdm import tqdm
from statistics import mean
import numpy as np
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort


def measure_search_time(sort_function, sz, repeats):
    """
    Возвращает результат замеров скорости выполнения сортировки
    """
    results = []
    for i in range(repeats):
        data = np.random.rand(sz)
        start = timer()
        sort_function(data)
        end = timer()
        results.append(end - start)
    return mean(results)


def main():
    algorithms = {
        'insertion_sort': lambda a: insertion_sort(a),
        'quick_sort': lambda a: quick_sort(a),
        'selection_sort': lambda a: selection_sort(a),
        'np_quicksort': lambda a: np.sort(a, kind='quicksort'),
        'np_mergesort': lambda a: np.sort(a, kind='mergesort')
    }

    sizes = list(range(1, 100, 5)) + list(range(200, 5000, 50))
    avg_time = {alg: [] for alg in algorithms}
    for sz in tqdm(sizes):
        for alg_name, f in algorithms.items():
            avg_time[alg_name].append(measure_search_time(f, sz, 100))

    for alg_name in algorithms:
        plt.plot(sizes, avg_time[alg_name], label=alg_name)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
