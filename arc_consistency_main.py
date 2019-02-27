from comparison import comp_by_nodes_time_domain, comp_by_edges_time_domain, single_run, anova_test_data_edge, \
    anova_test_data_node


def main():
    #single_run()
    comp_by_nodes_time_domain()
    comp_by_edges_time_domain()
    #anova_test_data_edge()
    #anova_test_data_node()


if __name__ == '__main__':
    main()
