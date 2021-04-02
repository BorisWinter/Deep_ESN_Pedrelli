import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

set_length = 20000 #20000 is the number we used for the parameter sweep initially
sampling_rate = 700
frequency = 60 #analogous to heart rate (per minute)
high = 0.5
low = -0.5

squarewave_array = np.zeros([set_length])

period = int(60 * sampling_rate / frequency)
print(period)

for t in range(set_length):
    if t%period < (period/2):
        squarewave_array[t] = high
    else:
        squarewave_array[t] = low

print(squarewave_array)
df = pd.DataFrame(squarewave_array)
plt.plot(squarewave_array)
plt.show()

df.to_csv('square_wave.csv')

