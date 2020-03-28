a = int(input())
b = int(input())

class KZI_21:
  def __init__(self,a, b):
   self.p1 = a
   self.p2 = b
   self.func(a,b)
def func(a,b):
  return (a*2+b*2)/2
print((func(a,b)))