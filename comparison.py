import matplotlib.pyplot as plt


def compare_by_time(time_ac1, time_ac2, time_ac3, time_ac4):
    x = ['AC_1', 'AC_2', 'AC_3', 'AC_4']
    y = [time_ac1, time_ac2, time_ac3, time_ac4]
    plt.xlabel('AC Algorithms')
    plt.ylabel('Run time (mS)')
    plt.title('Comparison using total running time')
    plt.grid(True)
    plt.plot(x, y, color="red", linewidth=2.5, linestyle='--')
    plt.show()
