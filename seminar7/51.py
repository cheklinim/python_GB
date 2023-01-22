"""
Напишите функцию same_by(characteristic, objects),
которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики,
и возвращают True, если это так.
Если значение характеристики для разных объектов отличается - то False.
Для пустого набора объектов, функция должна возвращать True.
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:							Вывод:
values = [0, 2, 10, 6]				same
if same_by(lambda x: x % 2, values):
	print(‘same’)
else:
	print(‘different’)
"""

def same_by(characteristic, objects):
    return len({characteristic(x) for x in objects}) == 1

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
	print('same')
else:
    print('different')

"""
def same_by (characteristic, object):
	result = True
	characteristicList = [characteristic(x) for x in object]
	for i in range(len(characteristicList) - 1):
		if characteristicList[i] != characteristicList[i + 1]:
			result = False
	return result


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
	print('same')
else:
	print('different')
"""
