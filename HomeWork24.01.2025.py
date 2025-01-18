# Написать функцию, которая принимает список чисел и возвращает их сумму.

def list_sum(numbers_list: list[int]) -> int:
    return sum(numbers_list)
numbers_list: list[int] = [i for i in range(5, 21)]
print(numbers_list)
print(list_sum(numbers_list))

# Создать функцию, которая принимает строку и возвращает количество гласных в ней.
from collections import Counter
def vowels (string) -> str:
    vowels_list: [list] = ('а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё', "a", "e", "i", "o", "u", "y")
    count_list:[list] = []
    count:[int] = 0
    string = string.lower().strip().replace(" ","")
    string_list:[list] = list(string)
    for vowel in string_list:
        if vowel in vowels_list:
            count +=1
            count_list.append(vowel)
    print(f"Количество гласных в строке: {count}")
    counted_list = Counter(count_list)
    for vowel, count in counted_list.items():
        print(f"Гласная '{vowel}' встречается: {count} раз") #
string = input('Введите строку: ')
vowels(string)

# Реализовать функцию, которая принимает два списка и возвращает их пересечение.
import random
def list_intersection(list1:list, list2:list) -> list:
    list1:list = set(list1)
    list2:list = set(list2)
    inter:list[int] = list(list1.intersection(list2))
    for i in inter:
        print(i)

list1:list[int] =[random.randint(1,100) for i in range(1, 10)]
list2:list[int] = [random.randint(1,100) for i in range(1,10)]
list_intersection(list1, list2)

# Создайте список городов, удалите один из них и добавьте два новых.
citis:list = ['Киров', 'Самара','Пермь', 'Москва', 'Липецк','Саратов', 'Владивосток']
citis.remove('Москва')
citis.append('Набережные Челны')
citis.append('Краснодар')
print(citis)

# Напишите программу, которая находит уникальные элементы двух множеств.
set_1 = {45, 3,12, 43, 9}
set_2 = {7, 12, 2, 23, 3}
unique_elements = set_1.symmetric_difference(set_2)
print(unique_elements)

# Создайте словарь студентов с баллами, найдите студента с максимальным баллом.
students = {'Петров': 10, 'Васичкин': 17, 'Куролесов': 8, 'Иванова': 20, 'Сидорова': 2}
max_value = max(students, key=students.get) #
print(max_value)