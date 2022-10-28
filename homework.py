string = input()
import math
lis = [float(i) for i in string.split(' ') if i.isdigit()]
if len(lis) == 3:
    d = lis[1] ** 2 - 4 * lis[0] * lis[2]
    if d > 0:
        x1 = (-lis[1] + math.sqrt(d)) / (2 * lis[0])
        x2 = (-lis[1] - math.sqrt(d)) / (2 * lis[0])
        print(f'x = {x1}, {x2}')
    elif d == 0:
        x = -lis[1] / (2 * lis[0])
        print(f'x = {x}')
    else:
        print("Корней нет")
else:
    print("Неверные входные данные")
