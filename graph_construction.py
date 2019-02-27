import copy
import random
from random import randint

import matplotlib.pyplot as plt
import networkx as nx

from constraints import def_constraints


def random_domain(domain_size):
    #rand_number = randint(10, domain_size)
    return random.sample(range(1, 1000), domain_size)


def construct_graph(total_nodes, edge_probability, domain_size):
    graph = nx.erdos_renyi_graph(total_nodes, edge_probability)
    # nx.draw(graph, with_labels=True)
    # plt.show()

    variables = []
    domains = {}
    for i in nx.nodes(graph):
        var = str(i)
        variables.append(var)
    variables = tuple(variables)

    for i in variables:
        domains.update({i: random_domain(domain_size)})
    print("Domains: ", domains)

    constraints = []
    for i in nx.edges(graph):
        x, y = i
        (n, m) = (y, x)
        rand_number = randint(1, 10)
        const, opposite = def_constraints(i, rand_number)
        constraints.append(const)
        constraints.append(((n, m), opposite))
    print("Constraints: ", constraints)
    domain1 = copy.deepcopy(domains)
    domain2 = copy.deepcopy(domains)
    domain3 = copy.deepcopy(domains)
    domain4 = copy.deepcopy(domains)

    return domain1, domain2, domain3, domain4, constraints
