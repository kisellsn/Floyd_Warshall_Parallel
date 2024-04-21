import time

import numpy as np
import pandas as pd

from graph_generator import generate_weighted_graph
from parallel import parallel_alg
from basic.basic_alg import floyd_warshall


if __name__ == '__main__':
    num_nodes = [100, 250, 500, 1000]  # Кількість вершин
    density = 0.3  # Щільність графу (ймовірність існування ребра між вершинами)
    weight_range = (1, 50)  # Діапазон ваг ребер

    data = []
    columns = ['Num Nodes', 'Basic', 'Parallel', 'SpeedUp']

    for nodes in num_nodes:
        graph = generate_weighted_graph(nodes, density, weight_range)

        start_time = time.time()
        basic_result = floyd_warshall(np.copy(graph))
        basic_time = time.time() - start_time

        start_time = time.time()
        parallel_result = parallel_alg.floyd_warshall_parallel(np.copy(graph))
        parallel_time = time.time() - start_time

        speed_up = basic_time / parallel_time

        data.append([nodes, basic_time, parallel_time, speed_up])
        print('Results equal : ', np.array_equal(basic_result, parallel_result))

    df = pd.DataFrame(data, columns=columns)
    print(df)
