# This is where we start

import numpy as np
import matplotlib.pyplot as plt

time,temperature = np.loadtxt("example_time_ vs_temperature_data.csv",delimiter=",",skiprows=1,unpack=True)

plt.figure() # Add a new figure to the memory
plt.plot(time,temperature)
plt.xlabel('Time[min]')
plt.ylabel('Temperature[°C]')
plt.savefig('time_temperature.png')