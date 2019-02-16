import copy
import random
from random import randint

import networkx as nx

from ac_1 import arc_consistency_1
from ac_2 import arc_consistency_2
from ac_3 import arc_consistency_3
from ac_4 import arc_consistency_4v2
from constraints import def_constraints


def random_domain():
    domain_size = 20
    return random.sample(range(-50, 50), domain_size)


def main():
    #total_nodes = randint(2, 100)
    #total_edges = randint(total_nodes - 1, 100)
    #G = nx.gnm_random_graph(total_nodes, total_edges)
    total_nodes = 3
    G = nx.erdos_renyi_graph(total_nodes, 1)
    #nx.draw(G, with_labels=True)
    #plt.show()
    # for v in nx.nodes(G):
    #     print('%s %d %f' % (v, nx.degree(G, v), nx.clustering(G, v)))

    #p = list(nx.edges(G))
    #print(p[0])
    #print(nx.edges(G))
    variables = []
    domains = {}
    for i in nx.nodes(G):
        var = str(i)
        variables.append(var)
    variables = tuple(variables)
    print(type(variables))

    #variables = ('0', '1', '2')

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
        #print("oppo", opposite)
        e, c = const
        constraints.append(const)
        #print((n, m))
        constraints.append(((n, m), opposite))

    # constraints = [
    #     ((0, 1), const_sqrt_val), ((1, 0), const_squared_val), ((0, 2), const_smaller), ((2, 0), const_bigger)
    # ]


        #print(i)
    print(constraints)

    #problem = CspProblem(variables, domains, constraints)
    #domain1 = domain2 = domain3 = domains
    domain1 = copy.deepcopy(domains)
    domain2 = copy.deepcopy(domains)
    domain3 = copy.deepcopy(domains)
    domain4 = copy.deepcopy(domains)

    import time
    start = time.time()
    print('\n')
    print("Before AC1   ", domain1)
    isConsistent = arc_consistency_1(domain1, constraints)
    print("After AC1   ", domain1)
    print("Status:   ", isConsistent)
    end = time.time()
    elapsed = (end - start) * 1000
    print("Elapsed time:   ", elapsed)

    start = time.time()
    print('\n')

    print("Before AC2   ", domain2)
    isConsistent = arc_consistency_2(domain2, constraints, total_nodes)
    print("After AC2   ", domain2)
    print("Status:   ", isConsistent)
    end = time.time()
    elapsed = (end - start) * 1000
    print("Elapsed time:   ", elapsed)

    start = time.time()
    print('\n')
    print("Before AC3   ", domain3)
    # arc_consistency_3(problem.domains, problem.constraints)
    isConsistent = arc_consistency_3(domain3, constraints)
    print("After AC3   ", domain3)
    print("Status:   ", isConsistent)
    end = time.time()
    elapsed = (end - start) * 1000
    print("Elapsed time:   ", elapsed)

    print('\n')
    start = time.time()

    print("Before AC4   ", domain4)
    isConsistent = arc_consistency_4v2(domain4, constraints)
    print("After AC4   ", domain4)
    print("Status:   ", isConsistent)
    end = time.time()
    elapsed = (end - start) * 1000
    print("Elapsed time:   ", elapsed)


main()
