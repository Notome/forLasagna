def task_1_7():
    cur = 1 
    n = 6 #факториал какого числа нам нужно найти
    print('Для вычисление факториала числа n, нужно найти произвдение всех чисел от 1 до n')
    for x in range(2, n + 1):
        print(f'Промежуточно для x = {x}, получаем {cur} * {x} = {cur*x}')
        cur *= x 
    print(cur)
#task_1_7()

def task_1_15():
    numerators = [1, 2] 
    denominators = [1, 1]
    
    print(f"Член 1: {numerators[0]}/{denominators[0]}")
    print(f"Член 2: {numerators[1]}/{denominators[1]}")

    for i in range(2, 5):  
        print(f"\nДля вычисления члена {i + 1}:")
        print(f"Предыдущие числители: {numerators[i-1]} (член {i}) + {numerators[i-2]} (член {i-1})")
        print(f"Предыдущие знаменатели: {denominators[i-1]} (член {i}) + {denominators[i-2]} (член {i-1})")

        new_numerator = numerators[i-1] + numerators[i-2]  
        new_denominator = denominators[i-1] + denominators[i-2]  
        
        numerators.append(new_numerator)
        denominators.append(new_denominator)
        
        print(f"Член {i + 1}: {new_numerator}/{new_denominator}")

    fifth_member = f"{numerators[4]}/{denominators[4]}"
    print(f"\n5-й член последовательности: {fifth_member}")
#task_1_15()

def task_2_4(x, epsilon=0.0001):
    num = 1  
    total_sum = 0  
    n = 0  

    print(f"\nНачинаем вычисления для x = {x} и ε = {epsilon}")

    while abs(num) >= epsilon:
        print(f"Член {n}: {num} (x^{2*n}) добавляется к сумме.")
        total_sum += num  
        print(f"Текущая сумма: {total_sum}")
        
        n += 1  
        num = x ** (2 * n)  
        print(f"Вызываем следующий член: {num} (x^{2*n})")

    print(f"Конечная сумма S = {total_sum}, номер итерации {n -1}")
#task_2_4(0.5)

def task_2_9():
    cuts = 0
    L = 0.1  
    D_A = 10e-10  
    print(f"Начальная длина нити: {L} м")
    print(f"Размер атома: {D_A} м")
    
    while L > D_A:
        cuts += 1
        L /= 2  
        print(f"После {cuts} разрезов длина нити: {L} м")
        
    print(f"Необходимо разрезать нить {cuts} раз(а), чтобы уменьшить длину до атома. Атом равен")
#task_2_9()

import math 

def task_3_5():
    a = math.pi / 5
    b = math.pi
    h = math.pi / 25
    epsilon = 0.0001
    res = 0
    print(f"Расчет значений s на промежутке [{a}, {b}] с шагом {h}:\n")

    while a <= b:
        result = 0
        i = 1
        add = ((-1) ** i * math.cos(i*a))/(i**2)

        while abs(add) > epsilon:
            result += add
            print(f"При x = {a}, i = {i}, добавляем: {add:} в сумму.")
            i += 1
            add = ((-1) ** i * math.cos(i*a))/(i**2)
            print(f'Общий ответ сейчас {res}, сумма ряда {result}')

        print(f'При x = {a}, аналитическая функция y = (x ** 2 - (pi ** 3 / 3))/4   равна: {(a ** 2 - (math.pi ** 2 / 3))/4}, сумма ряда: {result}')
        a += h
        res += add 
    print("\nЗавершено вычисление!")
    print(f'\nОтвет: {res}')
task_3_5()
