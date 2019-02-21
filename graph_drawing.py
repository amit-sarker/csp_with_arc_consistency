import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def compare_by_time(time_ac1, time_ac2, time_ac3, time_ac4):
    x = ['AC-1', 'AC-2', 'AC-3', 'AC-4']
    y = [time_ac1, time_ac2, time_ac3, time_ac4]
    plt.xlabel('AC Algorithms')
    plt.ylabel('Run time (mS)')
    plt.title('Comparison using total running time')
    plt.grid(True)
    plt.plot(x, y, color='b', linestyle='--', marker='D')
    plt.savefig("run_time_plot.eps")
    plt.show()


def compare_by_time_and_node(x, y1, y2, y3, y4, domain_size):
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Number of nodes')
    plt.ylabel('Run time (mS)')
    plt.title('Comparison using total running time vs number of nodes for domain size: %i' % domain_size)
    plt.grid(True)
    plt.plot(x, y1, color='y', linestyle='-', marker='.')
    plt.plot(x, y2, color='g', linestyle='--', marker='.')
    plt.plot(x, y3, color='r', linestyle=':', marker='.')
    plt.plot(x, y4, color='b', linestyle='-.', marker='.')
    plt.legend(['AC-1', 'AC-2', 'AC-3', 'AC-4'], loc='upper left')
    plt.savefig("run_time_vs_nodes.eps")
    plt.show()


def compare_by_time_and_edge(x, y1, y2, y3, y4, domain_size):
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Probability of edges')
    plt.ylabel('Run time (mS)')
    plt.title('Comparison using total running time vs probability of edges for domain size: %i' % domain_size)
    plt.grid(True)
    plt.plot(x, y1, color='y', linestyle='-', marker='.')
    plt.plot(x, y2, color='g', linestyle='--', marker='.')
    plt.plot(x, y3, color='r', linestyle=':', marker='.')
    plt.plot(x, y4, color='b', linestyle='-.', marker='.')
    plt.legend(['AC-1', 'AC-2', 'AC-3', 'AC-4'], loc='upper left')
    plt.savefig("run_time_vs_edges.eps")
    plt.show()
