"""
На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""

n = int(input())
ones = 0
zeros = 0
for i in range(n):
    x = int(input())
    if x == 1:
        ones += 1
    if x == 0:
        zeros += 1
print(min(ones, zeros))