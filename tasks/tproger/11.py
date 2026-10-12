# Посчитайте, сколько раз символ встречается в строке.

s = "Hello, Haskell!"

count = 0
for symbol in list(s):
  if symbol == 'l':
    count += 1

print(count)