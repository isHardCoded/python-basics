# Создайте класс Rectangle с методами для расчета площади и периметра и увелчение. Затем реализуйте несколько конкретных фигур.

class Rectangle:
  def __init__(self, width, height):
    self.__width = width
    self.__height = height

  @property
  def width(self):
    return self.__width

  @property
  def height(self):
    return self.__height

  @property
  def area(self):
    return self.width * self.height

  @property
  def perimeter(self):
    return 2 * (self.height + self.width)

  def scale(self, factor):
    self.width *= factor
    self.height *= factor