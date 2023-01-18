"""
Дана последовательность из N целых чисел и число K.
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
K – положительное число.

Input:   [1, 2, 3, 4, 5] k = 3
Output:  [4, 5, 1, 2, 3]
"""

list1 = [1, 2, 3, 4, 5]
k = int(input())

for j in range(k):
    temp = list1[0]
    for i in range(len(list1) - 1):
        list1[i] = list1[i+1]
    list1[-1] = temp

print(list1)

"""
list_1 = [5, 4, 6, 7, 8, -10]
k = int(input())
k = k % len(list_1)
list_result = list()
for i in range(k):
    list_result.append(list_1[len(list_1) - 1 - i])
for i in range(len(list_1) - k):
    list_result.append(list_1[i])
print(list_result)
"""
