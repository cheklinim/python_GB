"""
Дан массив, состоящий из целых чисел.
Напишите программу, которая в данном массиве определит количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного.
Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

Ввод: 			Ввод:
5				5
1 2 3 4 5		1 5 1 5 1

Вывод:			Вывод:
0				2

				(каждое число вводится с новой строки)
"""

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

count = 0
for i in range(1, len(array) - 1):
    if array[i - 1] < array[i] > array[i + 1]:
        count += 1
print(count)

"""
n = int(input())
list_first = list()
for i in range(n):
    x = int(input())
		list_first.append(x)
count = 0
for i in range(1, n - 1):
		if list_first[i - 1] < list_first[i] < list_first[i + 1]:
				count += 1
print(count)
"""
