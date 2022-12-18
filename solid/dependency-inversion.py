""" High level modules should not depend on low level modules, but rather depend on abstractions   """

from abc import ABC, abstractmethod
from enum import Enum

class Relationship(Enum):
  PARENT = 0
  CHILD = 1
  SIBLING = 2

class Person:
  def __init__(self, name):
    self.name = name
  
class Relationships:
  def __init__(self):
    self.relations = []
  
  def add_parent_and_child(self, parent, child):
    self.relations.append((parent, Relationship.PARENT, child))    
    self.relations.append((child, Relationship.CHILD, parent))


# Bad High level module
# we require the relationships to be store in a particular way - we have a dependecy on low level...
"""
class Research:
  def __init__(self, relationships):
    self.relations = relationships.relations
    for r in self.relations:
      if r[0].name == 'John' and r[1] == Relationship.PARENT:
        print(f'John has a child {r[2].name}')
"""

# Inferace (friendly so we know how to interface with higher level module)
class RelationshipBrowser:
  @abstractmethod
  def find_all_child_of(self, name): pass


class Relationships(RelationshipBrowser):
  def __init__(self):
    self.relations = []
  
  def add_parent_and_child(self, parent, child):
    self.relations.append((parent, Relationship.PARENT, child))    
    self.relations.append((child, Relationship.CHILD, parent))

  def find_all_child_of(self, name):
    for r in self.relations:
      if r[0].name == name and r[1] == Relationship.PARENT:
        yield r[2].name


class Research:
  def __init__(self, browser):
    for p in browser.find_all_child_of('John'):
      print(f'John has a chile called {p}')



if __name__ == "__main__":
  parent = Person('John')
  child1 = Person("Chris")
  child2 = Person('Bob')

  relationships = Relationships()
  relationships.add_parent_and_child(parent, child1)
  relationships.add_parent_and_child(parent, child2)

  Research(relationships)