""" Builder facet breaks the open close -> this one allows for extension"""

class Person:
  def __init__(self):
    self.name = None
    self.position = None
    self.DOB = None

  def __str__(self):
    return f'{self.name} born on {self.DOB} works as a {self.position}'

  @staticmethod
  def new():
    return PersonBuilder()


class PersonBuilder:
  def __init__(self):
    self.person = Person()
  
  def build(self):
    return self.person

class PersonInfoBuilder(PersonBuilder):
  def called(self, name):
    self.person.name = name
    return self
  
class PersonJobBuilder(PersonInfoBuilder):
  def works_at(self, position):
    self.person.position = position
    return self
  
class PersonDOBBuilder(PersonJobBuilder):
  def DOB_of(self, DOB):
    self.person.DOB = DOB
    return self



if __name__ == "__main__":

  pb = PersonDOBBuilder()

  me = pb\
      .called('Bob')\
      .works_at("Warehouse")\
      .DOB_of("11/03/99")\
      .build()

  print(me)