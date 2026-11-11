import random

class PickupError(Exception):
  pass

class Product:
  def __init__(self, name, price):
    if price <= 0:
      raise PickupError("Цена должна быть больше нуля.")
    self.name = name
    self.price = price

  def __str__(self):
    return f"{self.name} - ${self.price:.2f}"

class Order:
  counter = 0

  def __init__(self, customer, products):
    Order.counter += 1
    self.order_id = Order.counter
    self.customer = customer
    self.products = products
    self.status = "создан"
    self.code = None

  def total(self):
    return sum(p.price for p in self.products)
  
  def __str__(self):
    return f"Заказ №{self.order_id} | {self.customer} | {self.total()} ₽ | {self.status}"

class PickupPoint:
  def __init__(self, address, capacity):
    self.address = address
    self.capacity = capacity
    self.orders = {}

  def receive(self, order: Order):
    if len(self.orders) >= self.capacity:
      raise PickupError("Нет места на пункте")

    order.status = "на пункте"
    order.code = str(random.randint(1000, 9999))
    self.orders[order.order_id] = order

  def issue(self, order_id, code):
    if order_id not in self.orders:
      raise PickupError(f"Заказ №{order_id} не найден")

    order: Order = self.orders[order_id]

    if order.code != code:
      raise PickupError("Неверный код")

    order.status = "выдан"
    del self.orders[order_id]

  def refuse(self, order_id):
    if order_id not in self.orders:
      raise PickupError(f"Заказ №{order_id} не найден")

    order: Order = self.orders.pop(order_id)
    order.status = "возрат"

  def show(self):
    print(f"Пункт выдачи {self.address}: занято {len(self.orders)} из {self.capacity}")

    for order in self.orders.values():
      print(" ", order)

phone = Product("Телефон", 15000)
case = Product("Чехол", 500)
kettle = Product("Чайник", 2500)

point = PickupPoint("ул. Республики, 9", capacity=2)
o1 = Order("Анна", [phone, case])
o2 = Order("Иван", [kettle])
o3 = Order("Пётр", [case])

point.receive(o1)
point.receive(o2)

try:
    point.receive(o3)
except PickupError as e:
    print("Ошибка:", e)

point.show()

try:
    point.issue(1, "0000")
except PickupError as e:
    print("Ошибка:", e)

point.issue(1, o1.code)
point.refuse(2)
print(o1)
print(o2)
point.show()