# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []

for elem_a in a:
  for elem_b in b:
    if elem_a == elem_b:
      result.append(elem_a)

print(set(result))