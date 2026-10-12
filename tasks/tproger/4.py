# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды

def convert(seconds):
  minutes = seconds / 60

  hours = seconds / (60 * 60)
  days = seconds / (60 * 60 * 24)

  print(f"Минут: {minutes}")
  print(f"Часов: {hours}")
  print(f"Дней: {days}")
  print(f"Секунд: {seconds}")

print(convert(10000)) 