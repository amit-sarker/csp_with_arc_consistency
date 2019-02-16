import matplotlib.pyplot as plt


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
