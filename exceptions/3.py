def validate_password(password):
  if len(password) < 8:
      raise ValueError("пароль короче 8 символов")
  
  has_digit = any(char.isdigit() for char in password)
  has_upper = any(char.isupper() for char in password)
  
  if not has_digit:
    raise ValueError("в нём нет ни одной цифры")
  
  if not has_upper:
    raise ValueError("нет ни одной заглавной буквы")
  
  return True

passwords = ["123", "password", "Password", "Password1"]

for pwd in passwords:
    try:
        validate_password(pwd)
    except ValueError as e:
        print(f"'{pwd}': {e}")
    else:
        print(f"'{pwd}': ок")