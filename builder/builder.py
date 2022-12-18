""" Some objects are simple and can be created in a single call 
    others require alot of ceremony to create (having 10 init arguements is :/ )
  """
class HtmlElement:
  indent_size = 2

  def __init__(self, name="", text=""):
    self.name = name
    self.text = text
    self.elements = []

  def __str(self, indent):
    lines = []
    i = ' ' * (indent * self.indent_size)
    lines.append(f'{i}<{self.name}>')

    if self.text:
      i1 = ' ' * ((indent + 1) * self.indent_size)
      lines.append(f'{i1}{self.text}')

    for e in self.elements:
      lines.append(e.__str(indent + 1))

    lines.append(f'{i}</{self.name}>')
    return '\n'.join(lines)

  def __str__(self):
    return self.__str(0)

  @staticmethod
  def create(name):
      return HtmlBuilder(name)


class HtmlBuilder:

  def __init__(self, root_name):
    self.root_name = root_name
    self.__root = HtmlElement(name=root_name)

  # not fluent
  def add_child(self, child_name, child_text):
    self.__root.elements.append(
        HtmlElement(child_name, child_text)
    )

  # fluent
  def add_child_fluent(self, child_name, child_text): # allows you to change the invocations
    self.__root.elements.append(
         HtmlElement(child_name, child_text)
    )
    return self

  def clear(self):
    self.__root = HtmlElement(name=self.root_name)

  def __str__(self):
    return str(self.__root)


if __name__ == "__main__":

  # Simple (works ok)
  text = 'hello'
  parts = ['<p>', text, "</p>"]
  print("".join(parts))

  # More complicated is :/
  words = ['hello', 'world']
  parts = ['<ul>']
  for word in words:
    parts.append(f' <li>{word}</li>')
  parts.append('</ul>')
  print('\n'.join(parts))


  # ordinary non-fluent builder
  #builder = HtmlBuilder('ul')
  builder = HtmlElement.create('ul')
  builder.add_child('li', 'hello')
  builder.add_child('li', 'world')
  print('Ordinary builder:')
  print(builder)

  # fluent builder
  builder.clear()
  builder.add_child_fluent('li', 'hello') \
      .add_child_fluent('li', 'world') 
  print('Fluent builder:')
  print(builder)

