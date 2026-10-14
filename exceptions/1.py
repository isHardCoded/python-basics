while True:
    try:
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Введите число цифрами")
        continue 

    if age < 0 or age > 120:
        print("Некорректный возраст")
        continue

    break 

print(f"Регистрация продолжена, возраст: {age}")