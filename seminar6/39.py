"""
Даны два массива чисел.
Требуется вывести те элементы первого массива
(в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве.
Пользователь вводит  число N - количество элементов в первом массиве,
затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве.
Затем элементы второго массива
Ввод: 					Вывод:
7    					3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1			(каждое число вводится с новой строки)

"""

n = int(input())
array_n = []
for i in range(n):
    array_n.append(int(input()))

m = int(input())
array_m = []
for i in range(m):
    array_m.append(int(input()))

result = []
for item in array_n:
    if item not in array_m:
        result.append(item)
print(*result)

"""
n = int(input())
list_first = list()
for i in range(n):
    x = int(input())
		list_first.append(x)
m = int(input())
list_second = list()
for i in range(m):
    x = int(input())
		list_second .append(x)
count = 0
for i in range(n):
		for j in range(m):
				if list_first[i] == list_second[j]:
						count += 1
		if count != 0:
				print(list_first[i])
		count = 0
"""
