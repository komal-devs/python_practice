# a , b -> c
class Father:
  def skill1(self):
    print("coding")
class Mother():
  def skill2(self):
      print("cooking")
class Child(Father,Mother) :
  def skill3(self):
    print("drawing")

a = Child()
a.skill1()
a.skill2()
a.skill3()
    