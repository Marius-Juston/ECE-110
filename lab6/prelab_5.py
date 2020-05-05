import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

if __name__ == '__main__':
    voltage = np.array([8.837, 8.772, 8.759, 8.707, 8.688, 8.688, 8.627, 8.627, 8.586, 8.514, 8.375, 7.99])
    current = np.array([0.0006, 87.99, 93.6, 131.5, 148.9, 188.8, 215.2, 215.2, 258.4, 347.7, 534.9, 800])
    current /= 1000

    ax: Axes = plt.gca()
    ax.scatter(voltage, current, label="Battery Data")

    b, m = np.polynomial.polynomial.polyfit(voltage, current, 1)
    rt = 1 / m
    print(rt)
    print(b, m)
    print(-b / m)


    def eq(v):
        return m * v + b


    p = ax.plot([voltage.min(), -b / m], [eq(voltage.min()), 0], c='red', label=f"y={round(m, 3)}V+{round(b, 3)}")
    ax.minorticks_on()
    ax.grid(True)
    ax.set_title("mjuston2: IV Plot of real-life data")
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Current (A)")

    ax.legend()

    # ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.3f'))
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.3f'))

    plt.show()
