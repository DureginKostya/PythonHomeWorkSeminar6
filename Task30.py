'''Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое 
число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15'''
try:
    first_elm = int(input('Введите первый элемент арифметической прогрессии: '))
    difference = int(input('Введите разность между элементами арифметической прогрессии: '))
    number_elm = int(input('Введите количество элементов арифметической прогрессии: '))
    if number_elm > 0:
        arithmetic_progression = []
        for i in range(1, number_elm + 1):
            arithmetic_progression.append(first_elm + (i - 1) * difference)
        print('Арифметическая прогрессия:', end=' ')
        print(*arithmetic_progression)
    else:
        print('Введено недопустимое значение')
except:
    print('Введено недопустимое значение')