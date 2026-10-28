class Product:
  def __init__(self, name: str, price: float, quantity: int):
    if not name.strip():
      raise ValueError("Название товара не может быть пустым")

    if price <= 0:
      raise ValueError("Цена должна быть положительной")

    if quantity <= 0:
      raise ValueError("Количество должно быть положительным")

    self.name = name.strip()
    self.price = price
    self.quantity = quantity

  def get_total(self):
    return self.price * self.quantity

  def __str__(self):
    return f"{self.name} - {self.price} - {self.quantity}"


class Cart:
  def __init__(self):
    self.__products: list[Product] = []
    self.__discount = 0

  def add_product(self, name: str, price: float, quantity: int):
    for product in self.__products:
      if product.name.lower() == name.strip().lower():
        product.quantity += 1
        print(f"Количество товара изменено: {product.name}")
        return
    
    product = Product(name, price, quantity)
    self.__products.append(product)
    print(f"Товар добавлен: {product.name}")

  def remove_product(self, name: str):
    for product in self.__products:
      if product.name.lower() == name.strip().lower():
        self.__products.remove(product)
        print(f"Товар удален: {product.name}")
        return

    print("Товара нет в корзине")

  def get_subtotal(self):
    total = 0

    for product in self.__products:
      total += product.get_total()

    return total

  def apply_discount(self):
    subtotal = self.get_subtotal()

    if subtotal >= 300:
      self.__discount = 10
    else:
      self.__discount = 0

  def get_total(self):
    subtotal = self.get_subtotal()
    discount_amount = subtotal * self.__discount / 100

    return subtotal - discount_amount

  def show_cart(self):
    print("Товары в корзине:")

    for product in self.__products:
      print(product)

    self.apply_discount()

    print(f"Сумма: {self.get_subtotal()}")
    print(f"Скидка: {self.__discount}%")
    print(f"Итого: {self.get_total()}")

cart = Cart()

cart.add_product("Product 1", 100, 10)
cart.add_product("Product 2", 200, 1)

cart.show_cart()


    