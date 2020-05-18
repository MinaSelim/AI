class Node():

   def __init__(self, parent, pos):

      self.parent = parent
      self.pos = pos
      
      self.g = 0
      self.h = 0
      self.f = 0