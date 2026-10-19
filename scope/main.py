name = "John"

def create_greeting(greeting):
  greeting = "Hello"
  
  def say_hello(name):
    print(f"{greeting}, {name}!")

  say_hello()

create_greeting()