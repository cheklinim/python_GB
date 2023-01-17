"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
Помогите ему!
Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза.
Все числа натуральные и не превышают 30000.
"""

n = int(input())
min_value = 30001
max_value = -1
for i in range(n):
    x = int(input())
    min_value = min(min_value, x)
    max_value = max(max_value, x)
print(min_value, max_value)
