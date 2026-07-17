class Animal():
  def eating(self):
    print("eating")
class Dog(Animal):
  def bark(self):
    print("barks..")
class Cat(Animal):
  def meow(self):
    print("meows...")

d = Dog()
d.eating()
d.bark()

c = Cat()
c.eating()
c.meow()