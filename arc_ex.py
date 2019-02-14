from random import randint

import math
import networkx as nx
#import matplotlib.pyplot as plt
import sys

from ac_3 import arc_consistency_3, arc_consistency_1
from csp import CspProblem


def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


def random_domain():
    domain_size = 3
    var_domain = []
    for i in range(domain_size):
        val = randint(-50, 50)
        var_domain.append(val)
    return var_domain


def const_different(variables, values):
    return len(values) == len(set(values))


def const_one_odd_one_even(variables, values):
    if values[0] % 2 == 0:
        return values[1] % 2 == 1
    else:
        return values[1] % 2 == 0


def const_smaller(variables, values):
    return values[0] < values[1]


def const_bigger(variables, values):
    return values[0] > values[1]


def const_squared_val(variables, values):
    if values[1] < 0:
        return False
    return math.sqrt(values[1]) == values[0]


def const_gcd(variables, values):
    return gcd(values[0], values[1]) == 1


def const_sqrt_val(variables, values):
    if values[0] < 0:
        return False
    return math.sqrt(values[0]) == values[1]


def const_divisible(variables, values):
    if values[1] == 0:
        return False
    return values[0] % values[1] == 0


def const_multiple(variables, values):
    if values[0] == 0:
        return False
    return values[1] % values[0] == 0


def const_double(variables, values):
    return values[1] == 2 * values[0]


def def_constraints(edge, rand_number):
    const = []
    if rand_number == 1:
        const.append(edge)
        const.append(const_different)
        const = tuple(const)
        #print(const)
    elif rand_number == 2:
        const.append(edge)
        const.append(const_one_odd_one_even)
        const = tuple(const)
        #print(const)
    elif rand_number == 3:
        const.append(edge)
        const.append(const_smaller)
        const = tuple(const)
        #print(const)
    elif rand_number == 4:
        const.append(edge)
        const.append(const_bigger)
        const = tuple(const)
        #print(const)
    elif rand_number == 5:
        const.append(edge)
        const.append(const_squared_val)
        const = tuple(const)
        #print(const)
    elif rand_number == 6:
        const.append(edge)
        const.append(const_gcd)
        const = tuple(const)
        #print(const)
    elif rand_number == 7:
        const.append(edge)
        const.append(const_sqrt_val)
        const = tuple(const)
        #print(const)
    elif rand_number == 8:
        const.append(edge)
        const.append(const_divisible)
        const = tuple(const)
        #print(const)
    elif rand_number == 9:
        const.append(edge)
        const.append(const_multiple)
        const = tuple(const)
        #print(const)
    elif rand_number == 10:
        const.append(edge)
        const.append(const_double)
        const = tuple(const)
        #print(const)
    return const


def main():
    total_nodes = randint(2, 100)
    #total_edges = randint(total_nodes - 1, 100)
    #G = nx.gnm_random_graph(total_nodes, total_edges)
    G = nx.erdos_renyi_graph(3, 1)
    # for v in nx.nodes(G):
    #     print('%s %d %f' % (v, nx.degree(G, v), nx.clustering(G, v)))

    p = list(nx.edges(G))
    #print(p[0])
    #print(nx.edges(G))
    variables = []
    domains = {}
    for i in nx.nodes(G):
        var = str(i)
        variables.append(var)

    variables = tuple(variables)
    #print(type(variables))

    for i in variables:
        domains.update({i: random_domain()})
    print(domains)

    constraints = []
    nodes = []


    for i in nx.edges(G):
        #print(i)
        rand_number = randint(1, 10)
        constraints.append(def_constraints(i, rand_number))

    #problem = CspProblem(variables, domains, constraints)
    domain1 = domain2 = domain3 = domains

    print('\n')
    #print(constraints)
    print("Before AC1   ", domain1)
    #arc_consistency_3(problem.domains, problem.constraints)
    isConsistent = arc_consistency_1(domain1, constraints)
    print("After AC1   ", domain1)
    print("Status:   ", isConsistent)

    print('\n')

    print("Before AC3   ", domain3)
    # arc_consistency_3(problem.domains, problem.constraints)
    isConsistent = arc_consistency_3(domain3, constraints)
    print("After AC3   ", domain3)
    print("Status:   ", isConsistent)


main()