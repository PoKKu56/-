#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код
pi = 3.1415926
square = pi * (radius ** 2)
square = square.__round__(4)
print('Площадь круга равна',square)
# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
x = point[0]
y = point[1]
check = (x**2 + y**2)**.5
print(check.__round__(1))
print(check <= radius)


# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
x1 = point_2[0]
y2 = point_2[1]
check1 = ((x1**2)+(y2**2)**.5)
check1.__round__(1)
print(check1)
print(check1 <= radius)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


