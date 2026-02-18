import math

def f(x):
    return math.log10(x + 5) - math.cos(x)

def df(x):
    # Производная функции: 1 / ((x+5)*ln(10)) + sin(x)
    return 1 / ((x + 5) * math.log(10)) + math.sin(x)

eps = 0.001

# МЕТОД ХОРД
print("МЕТОД ХОРД")
print(f"{'Шаг':<5} | {'x_n':<8} | {'f(x_n)':<10} | {'x_n+1':<8} | {'Погрешность':<12}")
print("-" * 55)

# Неподвижный конец
a = -1.0      
fa = f(a)

# Начальное приближение (подвижный конец)
x_prev = 0.0  
step = 0

while True:
    fx = f(x_prev)

    # Формула метода хорд
    x_next = x_prev - (fx * (x_prev - a)) / (fx - fa)
    diff = abs(x_next - x_prev)
    
    print(f"{step:<5} | {x_prev:8.4f} | {fx:10.4f} | {x_next:8.4f} | {diff:12.4f}")
    
    if diff <= eps:
        break
    x_prev = x_next
    step += 1
print(f"Корень (хорды): {x_next:.4f}\n")


# МЕТОД НЬЮТОНА (КАСАТЕЛЬНЫХ)
print("МЕТОД НЬЮТОНА (КАСАТЕЛЬНЫХ)")
print(f"{'Шаг':<5} | {'x_n':<8} | {'f(x_n)':<10} | {'f\'(x_n)':<10} | {'x_n+1':<8} | {'Погрешность':<12}")
print("-" * 65)

# Начальное приближение
x_prev = -1.0 
step = 0

while True:
    fx = f(x_prev)
    dfx = df(x_prev)
    # Формула метода Ньютона
    x_next = x_prev - fx / dfx
    diff = abs(x_next - x_prev)
    
    print(f"{step:<5} | {x_prev:8.4f} | {fx:10.4f} | {dfx:10.4f} | {x_next:8.4f} | {diff:12.4f}")
    
    if diff <= eps:
        break
    x_prev = x_next
    step += 1
print(f"Корень (Ньютон): {x_next:.4f}")