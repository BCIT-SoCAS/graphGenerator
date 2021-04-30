import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random, randrange


def erdos_renyi(n, weighted, weight_range):
    V = set([v for v in range(n)])
    E = set()
    dict.fromkeys(range(n))
    for combination in combinations(V, 2):
        a = random()
        if a < 0.5:
            E.add(combination)
    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)
    if weighted:
        for (a, b) in g.edges():
            g.edges[a, b]['weight'] = randrange(1, weight_range)
    return g


print("How many nodes? ")
n = int(input())
print("Weighted? 0 -> No, 1 -> Yes")
weighted = bool(int(input()))
print("Spring or shell layout? 0 -> Spring, 1 -> Shell")
layout = bool(int(input()))
G = erdos_renyi(n, weighted, 10)
if layout:
    pos = nx.shell_layout(G)
else:
    pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title(f"Random Graph Generation with {n} nodes")
plt.show()
