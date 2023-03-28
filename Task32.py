'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]'''
from random import randint
try:
    number = int(input('Введите размерность массива: '))
    min_border = int(input('Введите минимальное значение диапазона: '))
    max_border = int(input('Введите максимальное значение диапазона: '))
    if number > 1 and min_border < max_border:       
        list_user = [randint(-50, 50) for _ in range(number)]
        print(f'Массив: {list_user}')
        list_ind = []
        for i in range(number):
            if min_border <= list_user[i] <= max_border:
                list_ind.append(i)
        if len(list_ind) != 0: 
            print(f'Индексы элементов входящих в диапазон от {min_border} до {max_border}: {list_ind}')
        else:
            print(f'В массиве нет элементов входящих в диапазон от {min_border} до {max_border}')
    else:
        print('Введено недопустимое значение')
except:
    print('Введено недопустимое значение')