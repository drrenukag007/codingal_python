class Robot:
  def __init__(self, name):
    self.name = name

  def together(self):
    print("we are your programmed companions, our names are:")



robot1 = Robot("Tom")

robot2 = Robot("Jerry")

robot1.together()
print(robot1.name)
print(robot2.name)
