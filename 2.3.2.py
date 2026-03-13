import numpy as np
import matplotlib.pyplot as plt

def phi(x):
    return 1/np.sin(x)

x = 1
eps = 0.001

while True:
    x_next = phi(x)
    if abs(x_next - x) < eps:
        break
    x = x_next

print("Корень:", x_next)

# график
x_vals = np.linspace(0.1,4,400)
y1 = x_vals*np.sin(x_vals)
y2 = np.ones_like(x_vals)

plt.plot(x_vals,y1,label="y = x*sin(x)")
plt.plot(x_vals,y2,label="y = 1")
plt.axvline(x_next, linestyle="--")

plt.legend()
plt.grid()
plt.title("График для задания 2")
plt.show()