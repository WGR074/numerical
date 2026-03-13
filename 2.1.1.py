import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1,4,400)

y1 = x**2
y2 = np.log10(x) + 6

plt.figure()
plt.plot(x,y1,label="y = x^2")
plt.plot(x,y2,label="y = lg(x) + 6")

plt.axhline(0)
plt.axvline(0)

plt.grid()
plt.legend()
plt.title("Задание 2.1")
plt.show()