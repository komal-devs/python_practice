class Vehicle :
  def general_usage(self) :
    print("General usage : to commute")
class MotorCycle(Vehicle) :
  def __init__(self) :
    print("I am motor cycle")
    self.wheels = 4
    self.roof = False
  def specific_usage(self) :
    
    self.general_usage()
    print("Specific usage :  road trip")

s = Vehicle()
t = MotorCycle()
t.specific_usage()
print(issubclass(MotorCycle,Vehicle))