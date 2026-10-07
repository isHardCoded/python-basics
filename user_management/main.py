from user_manager import *

users = []

while True:
  print("--- MENU ---")

  print("add - добавить пользователя")
  print("remove - удалить пользователя")
  print("list - показать список пользователей")
  print("exit - выход из программы")
  
  command = input("Введите команду: ")

  if command == "add":
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))

    add_user(users, name, age)

  elif command == "remove":
    id = int(input("Введите ID пользователя: "))
    remove_user(users, id)

  elif command == "list":
    list_users(users)

  elif command == "exit":
    print("Выход из программы...")
    break

  else:
    print("Неизвестная команда")
    break