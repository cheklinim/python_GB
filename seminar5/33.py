"""
Хакер Василий получил доступ к классному журналу и хочет заменить
все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот:
все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

n = int(input())
data = [int(x) for x in input().split()]
max_value = max(data)
min_value = min(data)

for i in range(len(data)):
    if data[i] == max_value:
        data[i] = min_value
print(*data)

"""
n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

max_number = max(list_1)
min_number = min(list_1)
for i in range(len(list_1)):
    if list_1[i] == max_number:
        list_1[i] = min_number
print(list_1)
"""
