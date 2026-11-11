import asyncio

# Меню: напиток -> список шагов (действие, сколько секунд занимает)
MENU = {
    "эспрессо": [("мелю зёрна", 1), ("варю эспрессо", 1)],
    "капучино": [("мелю зёрна", 1), ("варю эспрессо", 1), ("взбиваю молоко", 2)],
    "раф": [("мелю зёрна", 1), ("варю эспрессо", 1), ("взбиваю сливки с сиропом", 3)],
    "какао": [("грею молоко", 2), ("размешиваю какао", 1)],
    "матча": [("просеиваю порошок", 4), ("взбиваю с молоком", 2), ("добавляю сироп", 1)],
}

# Заказы: (имя клиента, напиток, сколько секунд клиент готов ждать)
ORDERS = [
    ("Алиса", "капучино", 5, 0),
    ("Борис", "эспрессо", 3, 0),
    ("Вика", "раф", None, 0),
    ("Гоша", "какао", 6, 2),
    ("Дима", "матча", 5, 0),
]

PRICES = {
    "эспрессо": 100,
    "капучино": 150,
    "раф": 200,
    "какао": 120,
    "матча": 180,
}

async def make_drink(customer, drink):
  if drink not in MENU:
    print(f"{customer}: напитка {drink} нет в меню")
    return None

  print(f"Принят заказ для {customer}: {drink}")

  for acion, seconds in MENU[drink]:
    print(f"{customer}: {acion}...")
    await asyncio.sleep(seconds)

  print(f"{customer}: {drink} готов!")
  return drink

async def serve(customer, drink, wait_time, arrival_time):
  if arrival_time > 0:
    await asyncio.sleep(arrival_time)
    print(f"{customer}: пришёл в кафе и заказал {drink}")
  
  try:
    result = await asyncio.wait_for(make_drink(customer, drink), timeout=wait_time)
  except asyncio.TimeoutError:
    print(f"{customer}: не дождался {drink} и ушёл")
    return None

  if result is not None:
    print(f"{customer}: получил {result}")

  return result

async def main():
  tasks = []

  for customer, drink, wait_time, arrival_time in ORDERS:
    tasks.append(asyncio.create_task(serve(customer, drink, wait_time, arrival_time)))

  await asyncio.sleep(1)
  tasks[3].cancel()
  print("Гоша: отменил заказ")

  results = await asyncio.gather(*tasks, return_exceptions=True)

  served = [r for r in results if isinstance(r, str)]
  revenue = sum(PRICES[drink] for drink in served)

  print(f"\nВыдано заказов: {len(served)} из {len(ORDERS)}")
  print(f"Выручка: {revenue} руб.")

  for r in served:
    print(f" - {r}")

asyncio.run(main())