import random
from random import randint

import copy
import networkx as nx

from constraints import def_constraints


def random_domain():
    domain_size = 1000
    return random.sample(range(-5000, 5000), domain_size)


def construct_graph():
    # total_nodes = randint(2, 100)
    # total_edges = randint(total_nodes - 1, 100)
    # G = nx.gnm_random_graph(total_nodes, total_edges)
    total_nodes = 3
    G = nx.erdos_renyi_graph(total_nodes, 1)
    # nx.draw(G, with_labels=True)
    # plt.show()
    # for v in nx.nodes(G):
    #     print('%s %d %f' % (v, nx.degree(G, v), nx.clustering(G, v)))

    # p = list(nx.edges(G))
    # print(p[0])
    # print(nx.edges(G))
    variables = []
    domains = {}
    for i in nx.nodes(G):
        var = str(i)
        variables.append(var)
    variables = tuple(variables)
    print(type(variables))

    # variables = ('0', '1', '2')

    # domains = {
    #     '0': [2, 4],
    #     '1': [1, 2],
    #     '2': [5, 6]
    # }

    for i in variables:
        domains.update({i: random_domain()})
    print(domains)

    constraints = []
    nodes = []

    for i in nx.edges(G):
        x, y = i
        (n, m) = (y, x)
        rand_number = randint(1, 10)
        const, opposite = def_constraints(i, rand_number)
        # print("oppo", opposite)
        e, c = const
        constraints.append(const)
        # print((n, m))
        constraints.append(((n, m), opposite))

    # constraints = [
    #     ((0, 1), const_sqrt_val), ((1, 0), const_squared_val), ((0, 2), const_smaller), ((2, 0), const_bigger)
    # ]

    # print(i)
    print(constraints)
    domain1 = copy.deepcopy(domains)
    domain2 = copy.deepcopy(domains)
    domain3 = copy.deepcopy(domains)
    domain4 = copy.deepcopy(domains)

    return domain1, domain2, domain3, domain4, constraints, total_nodes
