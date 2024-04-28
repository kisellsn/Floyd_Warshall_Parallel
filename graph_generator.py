import numpy as np
import random

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = np.full((num_nodes, num_nodes), np.inf)
        np.fill_diagonal(self.graph, 0)

    def generate_weighted_graph(self, density=0.3, weight_range=(1, 10)):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if i != j and random.random() < density:
                    weight = random.randint(weight_range[0], weight_range[1])
                    self.graph[i][j] = weight

    def get_graph(self):
        return self.graph

    def print_graph(self):
        for row in self.graph:
            print(row)

if __name__ == '__main__':
    num_nodes = 6  # Кількість вершин
    density = 0.3  # Щільність графу (ймовірність існування ребра між вершинами)
    weight_range = (-1, 20)  # Діапазон ваг ребер

    graph = Graph(num_nodes)
    graph.generate_weighted_graph(density, weight_range)
    graph_data = graph.get_graph()
    graph.print_graph()






