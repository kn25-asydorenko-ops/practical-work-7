import sys
import math

def solve():
    # Зчитуємо вхідні дані
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    x1, y1, r1, x2, y2, r2 = map(int, input_data)
    
    # Квадрат відстані між центрами кіл
    d_sq = (x1 - x2)**2 + (y1 - y2)**2
    
    # Сума та різниця радіусів
    r_sum = r1 + r2
    r_diff = abs(r1 - r2)
    
    r_sum_sq = r_sum**2
    r_diff_sq = r_diff**2
    
    # Визначення кількості точок перетину
    if d_sq == 0:
        if r1 == r2:
            print(-1)  # Кола збігаються (безкінечно багато точок)
        else:
            print(0)   # Концентричні кола з різними радіусами
    else:
        if d_sq > r_sum_sq or d_sq < r_diff_sq:
            print(0)   # Одне коло поза іншим або одне всередині іншого без дотику
        elif d_sq == r_sum_sq or d_sq == r_diff_sq:
            print(1)   # Зовнішній або внутрішній дотик
        else:
            print(2)   # Перетинаються у двох точках

if __name__ == '__main__':
    solve()