""" If you have some inteface that takes a base class you should be able 
to stick a derived class in and everything should work """


class Rectangle:
  def __init__(self, width, height):
    self._height = height #psuedo private
    self._width = width
  
  @property
  def area(self):
    return self._width * self._height
  
  def __str__(self):
    return f'Width : {self.width} Height: {self.height}'

  @property
  def width(self):
    return self._width
  
  @width.setter
  def width(self, value):
    self._width = value

  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, value):
    self._height = value


# This breaks the principle...
class Square(Rectangle):
  def __init__(self, size):
    Rectangle.__init__(self, size, size)

  @Rectangle.width.setter
  def width(self, value):
    self._width = self._height = value

  @Rectangle.height.setter
  def height(self, value):
    self._width = self._height = value


def test_case(rc):
  w = rc.width
  rc.height = 10
  expected = int(w * 10)

  print(rc.area)
  print(expected)



if __name__ == "__main__":
  
  rect = Rectangle(2, 3)
  test_case(rect) # okay  

  sq = Square(2)
  test_case(sq) # bad

  # Breaks the liskov subsituion princple as an interface using the base class 
  # should be able to use its derived class...
  # better of just having rectangle class ? or using factory class