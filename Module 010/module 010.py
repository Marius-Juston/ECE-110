import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

if __name__ == '__main__':
    with open('data-20200502-1713.circuitjs.txt', 'r') as file:
        time_step = float(file.readline().split(' ')[4])

        lines = tuple(map(int, file.readlines()))

        x = np.arange(0, len(lines)) * time_step

        fig: Figure = plt.figure(figsize=(11.69, 8.27))
        ax: Axes = fig.gca()
        ax.plot(x, lines)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Voltage (V)")
        ax.set_title("Audio Output (mjuston2)")

        fig.tight_layout()
        fig.savefig("figure.png")
        # plt.show()
