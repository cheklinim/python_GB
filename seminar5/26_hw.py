"""
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * power(x, y - 1)

a = int(input())
b = int(input())
print(power(a, b))
