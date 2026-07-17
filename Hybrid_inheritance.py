#  combination of multiple types inheritance
class A :
  def showA(self):
    print("Class A")
class B(A):
  def showB(self):
    print("Class B")
class C(A):
  def showC(self):
    print("Class C")
class D(B,C):
  def showD(self):
    print("Class D")

o = D()
o.showA()
o.showB()
o.showC()
o.showD()