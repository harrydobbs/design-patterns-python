""" When you add functionality you add it by extension rather than modification
    Open for extension, closed for modification  """

from abc import ABC, abstractmethod

# 1 - Our Customer Aldford wants us to build an application to calcuate the area of
# a list of triangles so we implment an area calculator 
# Later Aldford wants us to adjust the application so it can do circles as well
# We could implement another method (or way of checking the shape) , this is not ideal
# as potentially aldford might want us to later implement a method for triangles
# in a real world scenario where the code base is larger this is bad.


class Rectangle:
  def __init__(x:float, y:float):
    self.x = x
    self.y = y
  
class AreaCalculator:
  @staticmethod
  def area(rectangles):
    area = 0
    for rect in rectangles:
      area += rect.x * rect.y
    return area


# A better way of dealing with this is by implementing a base class:
# using the abc module is a good way to require that methods are implemented.

class Shape(ABC):
  @abstractmethod
  def area(self): pass

class Triangle(Shape):
  def __init__(self, base:float, height:float):
    self.base = base
    self.height = height
  
  @property
  def area(self):
    return 0.5 * self.base * self.height

class Circle(Shape):
  def __init__(self, radius:float):
    self.radius = radius
  
  @property
  def area(self):
    return 3.14 * self.radius ** 2

if __name__ == "__main__":
  
  triangles = []
  triangles.append(Triangle(5., 10.))
  triangles.append(Triangle(10., 100.))

  area = 0
  for triangle in triangles:
    area += triangle.area

  print(area) 

  circle = Circle(5.0)

