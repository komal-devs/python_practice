# a -> b-> c 
class Animal:
  def sound(self):
    print("Animal sound")
class Dog(Animal):
  def bark(self):
    print("Dog barks")
class Puppy(Dog):
  def cry(self):
    print("Puppy cries..")

p = Puppy()
p.sound()
p.bark()
p.cry()