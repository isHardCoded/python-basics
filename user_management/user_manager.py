from random import choices
from string import digits

def list_users(users: list):
  if len(users) == 0:
    print("Пользователей нет")
    return
    
  for user in users:
    print(user.get("id"), user.get("name"), user.get("age"))

def add_user(users: list, name, age):
  if name == None or age == None:
    print("Имя или возраст не заполнены")
    return
  
  if age <= 0 and age >= 90:
    print("Некорректный возраст")
    return

  id = ''.join(choices(digits, k=5))

  new_user = { "id": id, "name": name, "age": age }

  users.append(new_user)

def remove_user(users: list, id):
  for user in users:
    if user["id"] == str(id):
      users.remove(user)
      print("Пользователь удален")
    return
  print("Пользователь не найден")

  

