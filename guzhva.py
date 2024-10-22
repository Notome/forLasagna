def task_1_5(p, h):
    result = 0
    for i in range(10):
        term = p + i * h
        squared_term = term ** 2
        print(f'Текущий член прогрессии: {term}, его квадрат: {squared_term}')
        result += squared_term
        print(f'В данный момент ответ равен: {result}\n')
    print(f'Ответ: {result}')
#task_1_5(1, 1)

def task_1_13():
    x = -1.5
    while x < 1.5:
        if x <= -1: y = 1
        elif -1 < x <= 1: y = -x 
        else: y = -1  
        x += 0.1
        print(f'При x = {x}, y = {y}')
#task_1_13()

def task_2_2():
    L = 30000
    p = 1
    n = 1
    max_n = 1

    while p <= L:
        print(f'Текущий n: {n}, текущее произведение p: {p}')
        max_n = n  
        n += 3     
        p *= n     

    print(f'Наибольшее значение n: {max_n}')
    print(f'Потому что следующее значение будет n = {max_n + 3}, Произведение будет равно: {p * (max_n + 3)}, что больше {L}')
#task_2_2()

def task_2_6():
    initial_cells = 10
    target_cells = 105 #количество клеток которое нужно достичь
    division_time = 3 #количество часов для удваивания клеток
    total_time = 0
    current_cells = initial_cells

    print(f"Начальное количество клеток: {current_cells}")

    while current_cells < target_cells:
        current_cells *= 2
        total_time += division_time
        print(f"Количество клеток после {total_time} часов: {current_cells}")
    print(f"Общее время до достижения {target_cells} клеток: {total_time} часов")
#task_2_6()

import math

def task_3_4():
    a = 0.1
    b = 1
    h = 0.1
    epsilon = 0.0001
    res = 0
    print("Расчет значений s на промежутке [0.1, 1] с шагом 0.1:\n")

    while a <= b:
        result = 0
        i = 0
        add = ((2 * i + 1) * a ** (2 * i)) / math.factorial(i)

        while abs(add) > epsilon:
            result += add
            print(f"При x = {a}, i = {i}, добавляем: {add} в сумму.")
            i += 1
            add = ((2 * i + 1) * a ** (2 * i)) / math.factorial(i)
            print(f'Общий ответ сейчас {res}, сумма ряда {result}')

        print(f'При x = {a}, аналитическая функция y = (1+2x^2) * e^(x ^ 2) равна: {(1 + 2 * a ** 2) * math.e ** (a ** 2)}, сумма ряда: {result}')
        a += h
        res += add 
    print("\nЗавершено вычисление!")
    print(f'\n Ответ: {res}')
task_3_4()
