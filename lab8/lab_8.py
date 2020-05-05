import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

data = np.genfromtxt("Part 1 Matlab.txt", names=True)


def plot(ax, data, column):
    ax.plot(data['time'], data[column], label=column)


ax: Axes = plt.figure().gca()
plot(ax, data, 'Vvout1')
plot(ax, data, 'Vvout2')
ax.set_title("Part3 Tutorial: RC Circuits")
ax.set_xlabel("Time (sec)")
ax.set_ylabel("Output Voltage Across Capacitor (V)")
ax.legend()
ax.grid()

ax2 = plt.figure().gca()
plot(ax2, data, 'IC1')
plot(ax2, data, 'IC2')
ax2.set_title("Part3 Tutorial: RC Circuits")
ax2.set_xlabel("Time (sec)")
ax2.set_ylabel("Current Through the Capacitor (A)")
ax2.legend()
ax2.grid()

plt.show()
