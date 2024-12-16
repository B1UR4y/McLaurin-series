from math import *


def f3(x, n):
    answer = 1
    for i in range(1, n+1):
        answer += ((-1)**i) * (x**(2 * i) / factorial(2 * i))
    return answer


def f9(x, m, n):
    answer = 1
    for i in range(1, n+1):
        m_prod = m
        for j in range(1, i):
            m_prod *= (m - j)
        answer += (m_prod * x**i) / factorial(i)
    return answer


def menu(n = 5):
    while True:
        try:
            option = int(input("Выберите одну из опций:\n"
                         "1 - Функция 3 (cos(x))\n"
                         "2 - Функция 9 ((1 + x)^m)\n"
                         # "3 - Функция 10\n"
                         "4 - Выход\n"))
        except:
            print("Допустим только ввод целых чисел")
            continue
        match option:
            case 1:
                try:
                    x = float(input("Введите X: "))
                except:
                    print("Допустим только ввод чисел")
                    continue
                print(f3(x, n))
            case 2:
                try:
                    x = float(input("Введите X: "))
                    m = float(input("Введите M: "))
                except:
                    print("Допустим только ввод чисел")
                    continue
                if not -1 < x < 1:
                    print("X должен быть больше -1 и меньше 1")
                    continue
                print(f9(x, m, n))
            case 3:
                pass
            case 4:
                return 0
            case _:
                print("Допустим только ввод чисел от 1 до 3 включительно")
                # После добавление функции 10 - от 1 до 4


menu()