import random
from random import randint

import copy
import networkx as nx

from constraints import def_constraints, const_sqrt_val, const_squared_val, const_smaller, const_bigger


def random_domain():
    domain_size = 5
    return random.sample(range(-50, 50), domain_size)


def construct_graph2():
    total_nodes = 3

    variables = ('0', '1', '2')

    domains = {
        '0': [1, 4, 9, 15],
        '1': [1, 2, 3, 4],
        '2': [5, 6, 7, 8]
    }

    constraints = [
        ((0, 1), const_sqrt_val), ((1, 0), const_squared_val), ((0, 2), const_smaller), ((2, 0), const_bigger)
    ]

    print(constraints)
    domain1 = copy.deepcopy(domains)
    domain2 = copy.deepcopy(domains)
    domain3 = copy.deepcopy(domains)
    domain4 = copy.deepcopy(domains)

    return domain1, domain2, domain3, domain4, total_nodes, constraints

