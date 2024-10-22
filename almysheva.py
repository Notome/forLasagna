def task_1_1():
    result = 0

    for x in range(2, 36, 3):
        print(f'В данный момент ответ равен: {result}\nМы прибавляем число {x}\n')
        result += x 
        print(f'Получаем промежуточное значение: {result}')
    print(f'Ответ: {result}')
#task_1_1()

from math import factorial

def task_1_9():
    result = 0

    for x in range(1, 7):
        add = (-1) ** x * (5 ** x) / factorial(x) 
        print(f'В данный момент ответ равен: {result}\nМы прибавляем: (-1)^{x} * 5^{x}/{x}!, что равно: {add}')
        result += add
    print(f'Ответ: {result}')
#task_1_9()

from math import cos

def task_2_1(x):
    result, i, epsilon = 0, 1, 0.0001

    while True:
        add = cos(i * x) / (i ** i) 
        
        if abs(add) < epsilon:  # Check the added value instead of result
            print(f'Следующий член суммы по модулю равен {abs(add)}, что меньше {epsilon}')
            break
        print(f'В данный момент ответ равен: {result}\nМы прибавляем: cos({i}*{x})/{i}^{i}, что равно: {add}')
        result += add
        i += 1
    print(f'Ответ: {result}')
#task_2_1(5)

def task_2_7():
    initial_distance = 10  
    increase_rate = 0.10  
    total_distance = 0     
    total_distance_7_days = 0  
    daily_distance = initial_distance

    print("Расчёт суммарного пути за 7 дней:")
    for day in range(1, 8):
        total_distance_7_days += daily_distance
        print(f'День {day}: пробег {daily_distance} км')
        daily_distance *= (1 + increase_rate)

    print(f'Суммарный путь за 7 дней: {total_distance_7_days} км\n')

    daily_distance = initial_distance
    total_distance = 0
    days_to_100_km = 0

    print("Расчёт дней для суммарного пути 100 км:")
    while total_distance < 100:
        total_distance += daily_distance
        days_to_100_km += 1
        print(f'День {days_to_100_km}: суммарный путь {total_distance} км, пробег {daily_distance} км')
        daily_distance *= (1 + increase_rate)

    print(f'Спортсмен пробежит суммарный путь 100 км на {days_to_100_km} день.\n')

    daily_distance = initial_distance
    days_more_than_20_km = 0

    print("Расчёт дней для пробега больше 20 км в день:")
    while daily_distance <= 20:
        days_more_than_20_km += 1
        daily_distance *= (1 + increase_rate)
        print(f'День {days_more_than_20_km}: пробег {daily_distance} км')

    print(f'Спортсмен будет пробегать более 20 км на {days_more_than_20_km} день.')
#task_2_7()

import math

def task_3_8():
    a = 0.1
    b = 1
    h = 0.05
    epsilon = 0.0001
    res = 0
    print("Расчет значений s на промежутке [0.1, 1] с шагом 0.05:\n")

    while a <= b:
        result = 0
        i = 0
        add = (2 * a) ** i / math.factorial(i)

        while abs(add) > epsilon:
            result += add
            print(f"При x = {a}, i = {i}, добавляем: {add} в сумму.")
            i += 1
            add = (2 * a) ** i / math.factorial(i)
            print(f'Общий ответ сейчас {res}, сумма ряда {result}')

        print(f'При x = {a}, аналитическая функция y = e^(2x) равна: {math.e ** (2 * a)}, сумма ряда: {result:}')
        a += h
        res += add 
    print("\nЗавершено вычисление!")
    print(f'\n Ответ: {res}')
task_3_8()
