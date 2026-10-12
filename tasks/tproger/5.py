# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

values = input("Введите последовательность чисел: ")

list_of_values = values.split(", ")

numbers = map(int, list_of_values)

list_of_numbers = list(numbers)
tuple_of_numbers = tuple(list_of_numbers)

print(list_of_numbers)
print(tuple_of_numbers)