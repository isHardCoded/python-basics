class Table:
  def __init__(self, number, seats):
    self.number = number
    self.seats = seats
    self.guest_name = None
    self.reservation_time = None
    self.is_reserved = False

  def __str__(self):
    if self.is_reserved:
      return (f"Столик {self.number}: {self.seats} мест, занят")
    return f"Столик {self.number}: {self.seats} места, свободен"
    
class Restaurant:
  def __init__(self, name, tables):
    self.name = name
    self.tables = { table.number: table for table in tables }

  def get_table(self, table_number):
    if table_number not in self.tables:
      raise ValueError(f"Столика номер {table_number} не существует")
    return self.tables[table_number]

  def reserve(self, table_number, guest_name, guests, reservation_time):
    if not guest_name or not guest_name.strip():
      raise ValueError("Имя гостя не может быть пустым")

    if guests <= 0:
      raise ValueError("Количество гостей должно быть положительным")

    table: Table = self.get_table(table_number)

    if table.is_reserved:
      raise ValueError(f"Столик {table_number} занят")

    if guests > table.seats:
      raise ValueError(f"Столик не может вместить столько людей")

    table.is_reserved = True
    table.guest_name = guest_name.strip()
    table.reservation_time = reservation_time

    return f"Столик {table_number} забронирован на имя {guest_name} на {reservation_time}"

  def cancel(self, table_number):
    table: Table = self.get_table(table_number)

    if not table.is_reserved:
      raise ValueError("Столик уже свободен")

    table.is_reserved = False
    table.guest_name = None
    table.reservation_time = None

    return "Бронь отменена"

  def show_tables(self):
    return "\n".join(str(table) for table in self.tables.values())
  
rest = Restaurant("123", [Table(1, 2), Table(2, 2), Table(3, 2)])
print(rest.show_tables())

print(rest.reserve(1, "John", 1, "04-11-2026"))
print(rest.show_tables())

print(rest.reserve(2, "John", 2, "04-11-2026"))

print(rest.show_tables())