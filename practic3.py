import math

def phi(x):
    # Функция для итераций: x = -arccos(lg(x+5))
    return -math.acos(math.log10(x + 5))

# Начальное приближение и точность
x_prev = -1.0
eps = 0.001
step = 0

print("Метод простых итераций")
print(f"{'Шаг':<5} | {'x_n (старое)':<12} | {'x_n+1 (новое)':<13} | {'Погрешность':<12}")
print("-" * 50)

while True:
    # Вычисляем новое значение
    x_next = phi(x_prev)  
     # Считаем разницу        
    diff = abs(x_next - x_prev)   
    
    print(f"{step:<5} | {x_prev:12.4f} | {x_next:13.4f} | {diff:12.4f}")
    
    # Если достигли точности - останавливаем цикл
    if diff <= eps:               
        break
        
    x_prev = x_next
    step += 1

print(f"\nИтог: Корень x ≈ {x_next:.4f}")