'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

import random
n = int(input("Введите длинну массива"))
list_1 = []
for i in range(n):   # цикл заполнения массива случайными числами от 1 до 5 
    list_1.append(random.randint(1, 5))
print("Сгенерированный массив:")
print(list_1)
x = int(input("Введите число х"))
k = abs(x - list_1[0])  #  самый близкий элемнт массива будем определять вычитанием между Х и элементами массива. 
j = 0  # сюда записываем индекс эелемента массива с наименьшей разностью
for i in range(n):
    if abs(x - list_1[i]) < k:
        k= abs(x - list_1[i])   # если элемент массива дает дает меньшую разницу, то перезаписываем разность
        j = i   #  запоминаем номер элемента массива с наименьшей разностью

print(f"Cамый близкий по величине элемент к заданному числу {x} это {list_1[j]}")
