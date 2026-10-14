PRICES = {"хлеб": 50, "молоко": 90, "сыр": 400}

cart = [
    {"item": "хлеб", "qty": "2"},
    {"item": "молоко", "qty": "1"},
    {"item": "колбаса", "qty": "1"},
    {"item": "сыр", "qty": "много"},
    {"item": "сыр", "qty": "3"},
]

def calculate_total(cart):
  total = 0
  for position in cart:
    name = position["item"]
    quantity_text = position["qty"]

    try:
      price = PRICES[name]
      quantity = int(quantity_text)
    except KeyError:
      print(f"Товар '{name}' не найден в каталоге — пропущен")
    except ValueError:
      print(f"Некорректное количество у '{name}': '{quantity_text}' — пропущен")
    else:
      total += price * quantity

  return total

print(f"Итого: {calculate_total(cart)}")