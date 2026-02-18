import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x
x = np.linspace(-4.5, 2, 400)

# Определяем функции
# np.log10 - это десятичный логарифм (lg)
y1 = np.log10(x + 5)
y2 = np.cos(x)

# Настройка графика
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$y = \lg(x+5)$', color='blue', linewidth=2)
plt.plot(x, y2, label=r'$y = \cos(x)$', color='red', linewidth=2)

# Добавляем оси и сетку
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)

# Отмечаем интервал корня
plt.axvline(-1, color='green', linestyle=':', label='Граница x = -1')
plt.axvline(0, color='green', linestyle=':', label='Граница x = 0')

# Настройки отображения
plt.title('Графический метод отделения корней: $\lg(x+5) = \cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(-1.5, 1.5)
plt.xlim(-5, 2)

# Сохраняем график
plt.savefig('graphic_method_solution.png')