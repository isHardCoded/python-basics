list = [1, 2, 3, 4, 5]

def is_unique(list):
  for i in range(len(list)):
    for j in range(i + 1, len(list)):
      if list[i] == list[j]:
        return False

is_unique(list)