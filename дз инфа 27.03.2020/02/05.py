n = int(input())
if n == 1:
    n = "Linux"
else:
    n = "Windows"

class KZI_21:
  def __init__(self, a1="Оперционая", a2="система", a3=n):
   self.p1 = a1
   self.p2 = a2
   self.p3 = a3

ob1 = KZI_21()

print(ob1.p1, ob1.p2, ob1.p3)
