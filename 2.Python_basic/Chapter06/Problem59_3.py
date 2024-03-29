import matplotlib.pyplot as plt
import numpy as np


Fs = 8000  #sample rate 
f = 5      # the frequency of the signal 
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()