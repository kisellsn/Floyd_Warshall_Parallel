import random
import networkx as nx

import random
import numpy as np

def generate_weighted_graph(num_nodes, density=0.3, weight_range=(1, 10)):
    G = np.full((num_nodes, num_nodes), np.inf)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < density:
                weight = random.uniform(weight_range[0], weight_range[1])
                G[i][j] = weight
    np.fill_diagonal(G, 0)
    return G

if __name__ == '__main__':
    num_nodes = 6  # Кількість вершин
    density = 0.3  # Щільність графу (ймовірність існування ребра між вершинами)
    weight_range = (-1.0, 20.0)  # Діапазон ваг ребер
    weighted_digraph = generate_weighted_graph(num_nodes, density, weight_range)



    print(weighted_digraph)






