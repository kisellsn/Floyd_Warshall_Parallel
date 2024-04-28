import time
import pandas as pd
from graph_generator import Graph
from parallel import parallel_alg
from basic.basic_alg import floyd_warshall
import numpy as np

if __name__ == '__main__':
    graph = np.array([[0, 1, 2, 5, np.inf, np.inf, np.inf, np.inf, np.inf],
                      [np.inf, 0, np.inf, np.inf, np.inf, 11, np.inf, np.inf, np.inf],
                      [np.inf, np.inf, 0, np.inf, 9, 5, 16, np.inf, np.inf],
                      [1, np.inf, np.inf, 0, np.inf, np.inf, 3, np.inf, 1],
                      [np.inf, np.inf, np.inf, np.inf, 0, np.inf, np.inf, 18, np.inf],
                      [np.inf, np.inf, 1, np.inf, np.inf, 0, np.inf, 13, np.inf],
                      [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 2, np.inf],
                      [np.inf, 1, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf],
                      [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 1, np.inf, 0]])

    start_time = time.time()
    basic_result = floyd_warshall(np.copy(graph))
    basic_time = time.time() - start_time

    start_time = time.time()
    parallel_result = parallel_alg.floyd_warshall_parallel(np.copy(graph))
    parallel_time = time.time() - start_time

    print("Basic Time: ", basic_time)
    print("\nParallel Time: ", parallel_time)
    print('\nResults equal : ', np.array_equal(basic_result, parallel_result))

    df = pd.DataFrame(basic_result, index=range(len(basic_result)), columns=range(len(basic_result[0])))
    print(df)
