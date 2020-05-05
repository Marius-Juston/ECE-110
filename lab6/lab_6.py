import matplotlib.pyplot as plt
import numpy as np
import scipy.io

# Your file location will different than this test location
mat = scipy.io.loadmat('lab_6_data.mat')
current = mat['Trace_1_GetCH1CurrentMeasurement']
voltage = mat['Trace_1_GetCH1VoltageMeasurement']
# We re-define our variables and omit the last data point
current = current[0:-1]
voltage = voltage[0:-1]
# Example: If we want to ignore the first 3 values and last 2 values
# we can use the following commands
current = current[3:-2].flatten()
voltage = voltage[3:-2].flatten()

plt.plot(voltage, current, label='Original data points')
# Perform a polyfit on the data points voltage and current
# The corresponding coefficients for a 1st order polynomial are stored in p

start_moving_index = 7
end_moving_index = 5

x = voltage[start_moving_index:-end_moving_index]
y = current[start_moving_index:-end_moving_index]

b, m = np.polynomial.polynomial.polyfit(x=x, y=y, deg=1)

plt.plot(x, y)

print(f"{m}V + {b}")
print("R:", 1 / m)
print("Vop:", -b / m)

# Plot the linear model, in (m*V)+b form
plt.plot(voltage, voltage * m + b, label='$1^{st}$-order polynomial')
plt.title('Linear curve fitting')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.legend()
plt.text(.015, .95, f"I = {round(m, 4)}V + {round(b, 5)}\nR: {round(1 / m, 3)}Ω\nVop: {round(-b / m, 3)}V",
         # horizontalalignment='center',
         verticalalignment='center',
         transform=plt.gca().transAxes)
plt.tight_layout()

plt.grid('True')

plt.savefig("lab_6.png")
plt.show()
