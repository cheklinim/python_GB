"""
Напишите программу для печати всех уникальных значений в словаре.

Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
        {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально. Пользователь его не вводит
"""

source = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
        {" VIII ":" S007 "}]
result = set()
for item in source:
        for value in item.values():
                result.add(value.strip())
print(result)

"""
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
set_1 = set()
for i in list_1:
    for j in i:
        set_1.add(i[j])
print(set_1)
"""
