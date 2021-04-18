class Animals():
  
  def __init__(self, kind, sound):
    self.kind = kind
    self.sound = sound

  def __cat__(self):
    print()
    print('meow')

  def dog():
    print('vof')

  def say_type(self):
    print('this is ', self.kind)


class newClass(Animals):
  pass