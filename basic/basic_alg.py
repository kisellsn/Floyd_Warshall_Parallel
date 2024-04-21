import time

import numpy as np
import pandas as pd
from graph_generator import generate_weighted_graph


def floyd_warshall(graph):
    n = graph.shape[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


if __name__ == '__main__':
    num_nodes = [300]
    density = 0.3
    weight_range = (1, 50)

    print("Basic\n")
    data = []
    for num in num_nodes:
        graph = generate_weighted_graph(num, density, weight_range)
        start_time = time.time()
        result = floyd_warshall(graph)
        basic_time = time.time() - start_time
        data.append([num, basic_time])

    df = pd.DataFrame(data, columns=['Matrix Size', 'Time (s)'])
    print(df)
    # print(result)