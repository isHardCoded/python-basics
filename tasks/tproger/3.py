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