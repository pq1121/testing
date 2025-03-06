from __future__ import annotations
from os import system

def run():
    work = True

    while work:
        print("1. Задача №1 Квадратичное уравнение")
        print("0. Выход")
        num = input()

        if num == "1":
            system('cls')
            data = input_data_task1()
            quadratic_equation(data)
        elif num == "0":
            work = False


def input_data_task1():

    print(f'Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0')
    var = ["a", "b", 'c']

    for i in range(len(var)):
        var[i] = float(input(f"Введите {var[i]}= "))
    return var


def quadratic_equation(var: list[float]):
    from math import sqrt

    a, b, c = var[0], var[1], var[2]
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        print(f"Корни уравнения: {root1:.2f} и {root2:.2f}")

    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"Единственный корень уравнения: {root:.2f}")

    else:
        print('У уравнения нет действительных корней')
