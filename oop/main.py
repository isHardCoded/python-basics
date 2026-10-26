class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_age(self):
    return self.age

  def is_adult(self):
    return self.age >= 18

  def have_birthday(self):
    self.age += 1

  # Имя: John, Возраст: 25, Совершеннолетний: да
  def get_info(self):
    if self.is_adult():
      adult_status = "да"
    else:
      adult_status = "нет"
  
    print(f"Имя: {self.name}, Возраст: {self.age}, Совершеннолетний: {adult_status}")

user = User("John", 25)
user.get_info()
print(user.get_age())
user.have_birthday()
print(user.get_age())
