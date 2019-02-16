from comparison import compare_by_time
from graph_construction import construct_graph
from result import get_result


def main():
    domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints, total_nodes = construct_graph()
    time_ac1, time_ac2, time_ac3, time_ac4 = get_result(domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints, total_nodes)
    compare_by_time(time_ac1, time_ac2, time_ac3, time_ac4)


if __name__ == '__main__':
    main()
