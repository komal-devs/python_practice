class A :
  def show(self):
    print("Hello from  parent class")
class B(A) :
  def show(self):
    super().show()
    A.show(self)
    # parent method can be run along with child method using super or direct call
    print("Hello from child class")
o = B()
o.show()