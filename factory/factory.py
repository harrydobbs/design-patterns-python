""" Wholesale object creation (non-piecewise, unlike builder) """

from enum import Enum
 
from math import *

class CoordinateSystem(Enum):
  CARTESIAN = 1
  POLAR = 2

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f"{self.x} {self.y}"


  """ not possible , having logic in init is messy too... 
  def __init__(self, rho, theta):

  """

  """ Factory method allow us to init from polar or cartesian """

class PointFactory:

  @staticmethod
  def new_polar_point(x, y):
    return Point(x, y)
  
  @staticmethod
  def new_cartesian_point(rho, theta):
    return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":

  p1 = PointFactory.new_cartesian_point(3.14, 3.14 * 2)
  p2 = PointFactory.new_polar_point(2,3)

  print(p1,p2)
