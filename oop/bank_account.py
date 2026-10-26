class BankAccount:
  def __init__(self, balance):
    self.__balance = balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("Сумма должна быть положительной")

    self.__balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Сумма должна быть положительной")

    if amount > self.__balance:
      raise ValueError("Сумма не может быть больше баланса")

    self.__balance -= amount

account = BankAccount(100)
print(account.balance)