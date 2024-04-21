import time

import pandas as pd

from graph_generator import generate_weighted_graph
from parallel import parallel_alg
from basic.basic_alg import floyd_warshall
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Приклад використання:
    num_nodes = 100  # Кількість вершин
    density = 0.3  # Щільність графу (ймовірність існування ребра між вершинами)
    weight_range = (1, 50)  # Діапазон ваг ребер
    # graph = generate_weighted_digraph(num_nodes, density, weight_range)

    graph = np.array([[0, 1, 2, 5, np.inf, np.inf, np.inf, np.inf, np.inf],
                    [np.inf, 0, np.inf, np.inf, np.inf, 11, np.inf, np.inf, np.inf],
                    [np.inf, np.inf, 0, np.inf, 9, 5, 16, np.inf, np.inf],
                    [1, np.inf, np.inf, 0, np.inf, np.inf, 3, np.inf, 1],
                    [np.inf, np.inf, np.inf, np.inf, 0, np.inf, np.inf, 18, np.inf],
                    [np.inf, np.inf, 1, np.inf, np.inf, 0, np.inf, 13, np.inf],
                    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 2, np.inf],
                    [np.inf, 1, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf],
                    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 1, np.inf, 0]])
    print("Basic Time: ")
    start_time = time.time()
    basic_result = floyd_warshall(np.copy(graph))
    basic_time = time.time() - start_time
    print(basic_time,'\n')

    df = pd.DataFrame(basic_result, index=range(len(basic_result)), columns=range(len(basic_result[0])))
    print(df)


    print("\nParallel Time: ")
    start_time = time.time()
    parallel_result = parallel_alg.floyd_warshall_parallel(np.copy(graph))
    parallel_time = time.time() - start_time
    print(parallel_time)

    print("\nSpeed Up: " + str(basic_time/parallel_time))

    print('\nResults equal : ', np.array_equal(basic_result, parallel_result))


