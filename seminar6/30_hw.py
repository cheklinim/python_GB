"""
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

a1 = int(input("Введите значение первого элемента: "))
d = int(input("Введите значение разности: "))
n = int(input("Введите количество элементов: "))

array = []
for i in range(1, n + 1):
    array.append(a1 + (i - 1) * d)
print("Арифметическая прогрессия:", *array)
