import time

import numpy as np
import pandas as pd

from graph_generator import Graph
from parallel import parallel_alg
from basic.basic_alg import floyd_warshall


if __name__ == '__main__':
    num_nodes = [100, 500, 1000, 1500]
    density = 0.3
    weight_range = (1, 50)

    data = []
    columns = ['Num Nodes', 'Basic', 'Parallel', 'SpeedUp']
    for nodes in range(len(num_nodes)):
        graph = Graph(num_nodes[nodes])
        graph.generate_weighted_graph(density, weight_range)

        start_time = time.time()
        floyd_warshall(np.copy(graph.get_graph()))
        basic_time = time.time() - start_time

        start_time = time.time()
        parallel_alg.floyd_warshall_parallel(np.copy(graph.get_graph()))
        parallel_time = time.time() - start_time

        speed_up = basic_time / parallel_time

        data.append([num_nodes[nodes], round(basic_time, 2), round(parallel_time, 2), speed_up])

    df = pd.DataFrame(data, columns=columns)
    print(df)
