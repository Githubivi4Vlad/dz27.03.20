a = int(input())
b = int(input())

class KZI_21:
  def __init__(self, a, b):
   self.p1 = a
   self.p2 = b
   self.func(a,b)
def func(a,b):
  if a>b:
   return a*b 
  else:
   return b/a
print((func(a,b)))