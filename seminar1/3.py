"""
В некоторой школе решили набрать три новых математических класса
и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся.
Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.

**Input:**
20
21
22

**Output:**
32
"""

a = int(input())
b = int(input())
c = int(input())
print((a+b+c) // 2 + int((a+b+c) % 2 != 0))

"""
a = int(input())
b = int(input())
c = int(input())
a1 = (a + 1) // 2
b1 = (b + 1) // 2
c1 = (c + 1) // 2
s = a1 + b1 + c1
print(s)
"""
