""" Don't want too many methods in an interface  """
from abc import ABC, abstractmethod


class Machine:
  def print(self, document):
    raise NotImplementedError
  def fax(self, document):
    raise NotImplementedError
  def scan(self, document):
    raise NotImplementedError


""" Its bad having all the methods in the inteface 
    as it looks like the child classes has methods avaliable """

class OldFashionedPrinter(Machine):
  def print(self, document):
    # ok
    pass
  
  def fax(self, document):
    pass #noop

  def scan(self, document):
    """ Not supported """
    pass #noop


""" Idea is to keep the interface granular """

class Printer:
  @abstractmethod # must be declared in child class
  def print(self, document):
    pass

class Fax:
  @abstractmethod
  def fax(self, document):
    pass

class Scanner:
  @abstractmethod
  def scan(self, document):
    pass


class MyPrinter(Printer):
  def print(self, document):
    pass


class Photocopier(Printer, Scanner):
  def print(self, document):
    pass
  
  def scan(self, document):
    pass

class MultiFunctionDevice(Printer, Scanner):
  @abstractmethod
  def print(self, document):
    pass

  @abstractmethod
  def scan(self, document):
    pass


class MultiFunctionMachine(MultiFunctionDevice):
  def __init__(self, printer, scanner):
    self.scanner = scanner
    self.printer = printer
  
  def print(self, document):
    self.printer.print(document)
  
  def scan(self, document):
    self.scanner.scan(document)



if __name__ == "__main__":

  my_printer = MyPrinter()

