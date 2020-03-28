class KZI_21:
  def __init__(self, a1="Днистер", a2="Десна"):
   self.p1 = a1
   self.p2 = a2
ob1 = KZI_21("Днипро","Ворскла")
ob2 = KZI_21("Днипро")
ob3 = KZI_21("                ")
print(ob1.p1, ob1.p2)
print(ob2.p1)
print(ob3.p1)