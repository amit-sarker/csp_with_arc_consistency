from graph_construction import construct_graph
from graph_drawing import compare_by_time_and_node, compare_by_time_and_edge
from result import get_result


def single_run():
    total_nodes = 5
    edge_probability = 1
    domain_size = 100
    cnt = 0
    c = 0

    while True:
        if c >= 100:
            break
        domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints = construct_graph(total_nodes, edge_probability, domain_size)
        time_ac1, time_ac2, time_ac3, time_ac4, is_same, is_const = get_result(domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints, total_nodes)

        if is_const:
            c += 1
            if is_same:
                cnt += 1
    print("Total:  ", cnt)


def comp_by_nodes_time_domain():
    total_nodes = 5
    edge_probability = 0.5
    domain_size = 10
    while True:
        if domain_size > 100:
            break
        x = []
        y1 = []
        y2 = []
        y3 = []
        y4 = []
        while True:
            if total_nodes >= 100:
                break
            time1 = 0
            time2 = 0
            time3 = 0
            time4 = 0
            for i in range(200):
                domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints = construct_graph(total_nodes, edge_probability, domain_size)
                time_ac1, time_ac2, time_ac3, time_ac4, is_same, consistent = get_result(domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints, total_nodes)
                time1 += time_ac1
                time2 += time_ac2
                time3 += time_ac3
                time4 += time_ac4
            x.append(total_nodes)
            y1.append(time1 / 200)
            y2.append(time2 / 200)
            y3.append(time3 / 200)
            y4.append(time4 / 200)
            total_nodes += 5
        compare_by_time_and_node(x, y1, y2, y3, y4, domain_size)
        domain_size += 30
        total_nodes = 5


def comp_by_edges_time_domain():
    total_nodes = 50
    edge_probability = 0.1
    domain_size = 10
    while True:
        if domain_size > 100:
            break
        x = []
        y1 = []
        y2 = []
        y3 = []
        y4 = []
        while True:
            if edge_probability > 1:
                break
            time1 = 0
            time2 = 0
            time3 = 0
            time4 = 0
            for i in range(200):
                domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints = construct_graph(total_nodes, edge_probability, domain_size)
                time_ac1, time_ac2, time_ac3, time_ac4, is_same, consistent = get_result(domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints, total_nodes)
                time1 += time_ac1
                time2 += time_ac2
                time3 += time_ac3
                time4 += time_ac4
            x.append(edge_probability)
            y1.append(time1 / 200)
            y2.append(time2 / 200)
            y3.append(time3 / 200)
            y4.append(time4 / 200)
            edge_probability += 0.1
        compare_by_time_and_edge(x, y1, y2, y3, y4, domain_size)
        domain_size += 30
        edge_probability = 0.1
