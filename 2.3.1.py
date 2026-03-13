import numpy as np
import matplotlib.pyplot as plt

# функция итерации
def phi(x):
    return np.sqrt(np.log10(x) + 6)

# метод простых итераций
x = 2
eps = 0.001

while True:
    x_next = phi(x)
    if abs(x_next - x) < eps:
        break
    x = x_next

print("Корень:", x_next)

# построение графика
x_vals = np.linspace(0.5,4,400)
y1 = x_vals**2
y2 = np.log10(x_vals) + 6

plt.plot(x_vals,y1,label="y = x^2")
plt.plot(x_vals,y2,label="y = lg(x) + 6")
plt.axvline(x_next, linestyle="--")

plt.legend()
plt.grid()
plt.title("График для задания 1")
plt.show()

