from abc import ABC

class HotDrink(ABC):
  def consume(self):
    pass

class Tea(HotDrink):
  def consume(self):
    print("this tea is bad")

class Coffee(HotDrink):
  def consume(self):
    print("This Coffee is bad")


class HotDrinkFactory(ABC): # kinda pointless in python but tells you what kinda API to implement...
  def prepare(self, amount):
    pass

class TeaFactory(HotDrinkFactory):
  def prepare(self, amount):
    print(f"Put in tea bag, boil add milk {amount}")
    return Tea()

class CoffeeFactory(HotDrinkFactory):
  def prepare(self, amount):
    print(f"Put in coffee bag, add milk {amount}")
    return Coffe()


class HotDrinkMachine:
  class AvaliableDrink(Enum):
    COFFEE = auto()
    TEA = auto()

  factories = []
  initalized = False

  def __init__(self):
    if not self.initalized:
      self.initalized = True
      for d in self.AvaliableDrink:
        name = d.name[0] + d.name[1:].lower()
        factory_name = name + "Factory"
        factory_instance = eval(factory_name)()
        self.factories.append((name, factory_instance))

  def make_drink(self):
    print("Avaliable")
    for f in self.factories:
      print(f[0])
    
    s = input(f'Please pick drink 0 - {len(self.factories) - 1}:')
    idx = int(s)
    s = input(f'Amount :')
    amount = int(s)
    return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
  entry = input("What kind of drink you want?")

  drink = make_drink(entry)

