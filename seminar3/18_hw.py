"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
"""

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
x = int(input())
result = array[0]
for item in array:
    if abs(item - x) < abs(result - x):
        result = item
print(result)
