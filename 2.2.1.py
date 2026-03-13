import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,400)

y1 = x*np.sin(x)
y2 = np.ones_like(x)

plt.figure()
plt.plot(x,y1,label="y = x*sin(x)")
plt.plot(x,y2,label="y = 1")

plt.axhline(0)
plt.axvline(0)

plt.grid()
plt.legend()
plt.title("Задание 2.2")
plt.show()