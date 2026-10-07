# Есть список numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

# Даны списки:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].

# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []

for elem_a in a:
  for elem_b in b:
    if elem_a == elem_b:
      result.append(elem_a)

print(set(result))

# Отсортируйте словарь по значению в порядке возрастания и убывания
d = {
  1: 2, 
  3: 4, 
  4: 3, 
  2: 1, 
  0: 0
}

result = {}
used = []

for i in range(len(d)):
  min_key = None

  for key in d:
    if key not in used:
      if min_key is None or d[key] < d[min_key]:
        min_key = key

  result[min_key] = d[min_key]
  used.append(min_key)

print(result)

# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды

def convert(seconds):
  minutes = seconds / 60

  hours = seconds / (60 * 60)
  days = seconds / (60 * 60 * 24)

  print(f"Минут: {minutes}")
  print(f"Часов: {hours}")
  print(f"Дней: {days}")
  print(f"Секунд: {seconds}")

print(convert(10000)) 

# Дней: 0.1
# Часов: 2.7
# Минут: 166
# Секунд: 10000