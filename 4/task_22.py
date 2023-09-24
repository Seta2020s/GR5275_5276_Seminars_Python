"""Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств."""

n = int(input("Введите количество элементов в первом наборе: "))
m = int(input("Введите количество элементов во втором наборе: "))
dict1 = {}
dict2 = {}
print("Введите элементы первого набора:")
for _ in range(n):
    element = int(input())
    dict1[element] = dict1.get(element, 0) + 1
print("Введите элементы второго набора:")
for _ in range(m):
    element = int(input())
    dict2[element] = dict2.get(element, 0) + 1
common_elements = set(dict1.keys()) & set(dict2.keys())
sorted_common_elements = sorted(common_elements)
print("Элементы, встречающиеся в обоих наборах в порядке возрастания:")
for element in sorted_common_elements:
    print(element)
