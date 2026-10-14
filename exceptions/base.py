def set_age(age):
  if age < 0:
    raise ValueError("Возраст не может быть отрицательным")
  return age

try:
  set_age(-5)
except Exception as e:
  print(f"Error: {e}")