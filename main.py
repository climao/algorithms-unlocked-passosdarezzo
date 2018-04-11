# -*- coding: utf-8 -*-

import algorithms as algo
from benchmark import *

a = generate_random_list(100, 1, 100000)

# FIND
benchmark(algo.linear_search, a, a[40])

benchmark(algo.better_linear_search, a, a[40])

benchmark(algo.sentinel_linear_search, a, a[40])

benchmark(algo.binary_search, a, a[40])

# SORT
benchmark(algo.selection_sort, generate_random_list(100, 1, 100000))

benchmark(algo.insertion_sort, generate_random_list(100, 1, 100000))
