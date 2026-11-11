# Разработайте класс Student, который хранит информацию о студенте: имя, список курсов и оценки. Реализуйте методы для расчета среднего балла и добавления новых курсов.

class Student:
  def __init__(self, name: str):
    self.__name = name
    self.__courses = {}

  @property
  def courses(self):
    return self.__courses
  
  @property
  def name(self):
    return self.__name

  def average(self):
    average_grades = []

    for grades in self.__courses.values():
      average_grades.append(sum(grades) / len(grades))

    return average_grades

  def add_course(self, name):
    if name in self.__courses:
      return f"{name} уже существует"
    
    self.__courses[name] = []
    return f"{name} успешно добавлен"

  def add_grade(self, course_name: str, grade: int):
    if not course_name in self.courses:
      return f"{course_name} не существует"

    self.courses[course_name].append(grade)
    return "Оценка добавлена"

  def __str__(self):
    return f"{self.name}: {self.courses}"

s = Student("Petya")
print(s)