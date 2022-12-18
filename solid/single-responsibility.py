""" Class should only do it's primary reponsability and not take on additional ones """

# This is good 
class ShoppingList:
  def __init__(self):
    self.entries =[]
    self.count = 0
  
  def add_entry(self, text):
    self.entries.append(f"{self.count}: {text}")
    self.count += 1

  def remove(self, pos):
    del self.entries[pos]
  
  def __str__(self):
    return "\n".join(self.entries)


# This is bad 
# We have added an additional responsibility (loading / saving)
class ShoppingListAntiPattern:
  def __init__(self):
    self.entries =[]
    self.count = 0
  
  def add_entry(self, text):
    self.entries.append(f"{self.count}: {text}")
    self.count += 1

  def remove(self, pos):
    del self.entries[pos]
  
  def __str__(self):
    return "\n".join(self.entries)
  
  def save(self, filename):
    file = open(filename, 'w')
    file.write(str(self))
    file.close()
  
  def load(self, filename):
    pass


# Better to implment an additional class to do the loading / saving
class PersistenceManager:
  @staticmethod
  def save_to_file(shopping_list, filename):
    file = open(filename, 'w')
    file.write(str(shopping_list))
    file.close()


if __name__ == "__main__":

  shopping_list = ShoppingList()
  persistence_manager = PersistenceManager() 

  shopping_list.add_entry("Eggs")
  shopping_list.add_entry("Milk")
  shopping_list.add_entry("Butter")

  persistence_manager.save_to_file(shopping_list, "my shopping list")
  print(shopping_list)
  

  