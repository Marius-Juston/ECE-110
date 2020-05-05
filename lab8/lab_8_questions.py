import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

data = np.genfromtxt("Part 1 Matlab Questions.txt", names=True)


def plot(ax, data, column):
    ax.plot(data['time'], data[column], label=column)


def draw_figure(*a, title, y_label, file_name):
    fig: Figure = plt.figure()
    ax: Axes = fig.gca()
    for el in a:
        plot(ax, data, el)
    ax.set_title(title)
    ax.set_xlabel("Time (sec)")
    ax.set_ylabel(y_label)
    ax.legend()
    ax.grid()
    fig.savefig(file_name)


def find_closest_value_index(array, x):
    return (np.abs(array - x)).argmin()


draw_figure("Vvout1", title="Part 1: RC Circuits UIN: 675078771",
            y_label="Output Voltage Across Capacitor (V)",
            file_name="Part 1 Question 2")

voltage = data['Vvout1']
time = data['time']
t_10 = find_closest_value_index(voltage, 1)
t_90 = find_closest_value_index(voltage, 9)

print(time[t_10], time[t_90], time[t_90] - time[t_10], (time[t_90] - time[t_10]) / 2.2)

plt.tight_layout()
plt.show()
