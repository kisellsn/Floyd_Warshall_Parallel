
import time
import pandas as pd

from graph_generator import generate_weighted_graph
from joblib import Parallel, delayed

def worker(args):
    i, row, n, k, rowK = args
    for j in range(n):
        row[j] = min(row[j], row[k] + rowK[j])
    return i, row

def floyd_warshall_parallel(graph, n_jobs=-1):
    n = graph.shape[0]
    with Parallel(n_jobs=n_jobs) as parallel:
        for k in range(n):
            result_list = parallel(delayed(worker)((i, graph[i], n, k, graph[k])) for i in range(n))
            for i, res in result_list:
                graph[i] = res
    return graph


if __name__ == '__main__':
    num_nodes = [100, 250, 500, 1000]
    num_threads = [-1, 2, 3, 4, 5, 6, 7, 8, 9]
    density = 0.3
    weight_range = (1, 50)

    print("Parallel\n")
    data = []
    for threads in range(60):
        row_data = [threads]
        for num in num_nodes:
            graph = generate_weighted_graph(num, density, weight_range)
            start_time = time.time()
            result = floyd_warshall_parallel(graph)
            execution_time = time.time() - start_time
            row_data.append(execution_time)
        data.append(row_data)

    columns = ['Num Proc|Num Nodes'] + ['{} nodes'.format(num) for num in num_nodes]
    df = pd.DataFrame(data, columns=columns)
    print(df)



