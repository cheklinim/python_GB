"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

5
1 2 3 4 5
3
-> 1
"""

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
x = int(input())
"""count = 0
for item in array:
    if item == x:
        count += 1
print(count)
"""
print(array.count(x))
