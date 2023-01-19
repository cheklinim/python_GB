"""
Дан список чисел.
Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод:			Вывод:
1 2 3 2 3			2
"""

array = [int(x) for x in input().split()]
count = 0
for item in array:
    if array.count(item) == 2:
        count += 1
print(count//2)

"""
list_1 = [1, 2, 3, 2, 3]
count = 0
for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if i != j and list_1[i] == list_1[j]:
            count += 1
print(count)
"""
