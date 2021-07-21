#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
width = len(my_favorite_movies)
first_film = my_favorite_movies[0:10]
print('Первый фильм: ', first_film)
last_film = my_favorite_movies[width-15: width]
print('Последний фильм: ', last_film)
second_film = my_favorite_movies[12:25]
print('Второй фильм: ', second_film)


# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
