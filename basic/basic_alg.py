
def floyd_warshall(graph):
    n = graph.shape[0]
    result_graph = [[0 if i == j else graph[i][j] if graph[i][j] is not None else float('inf') for j in range(n)] for i
                    in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result_graph[i][j] = min(result_graph[i][j], result_graph[i][k] + result_graph[k][j])
    return result_graph
