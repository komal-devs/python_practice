class Accident(Exception):
  def __init__(self,msg):
    self.msg = msg
  def printException(self):
    print("User defined Exception ",self.msg)
  def handle(self):
    print("Accident occurred take detour")

try :
  raise Accident('Crash between two cars')
except Accident as e :
  e.printException()
  e.handle()
