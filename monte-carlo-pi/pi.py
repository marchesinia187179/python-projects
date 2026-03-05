import random
import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setNewPoint(self):
        self.x = random.random()
        self.y = random.random()

    def getDistanceFromOrigin(self):
        return math.hypot(self.x, self.y)

point = Point()

correctTests = 0
totalTests = 10000000
for i in range(totalTests):
    point.setNewPoint()
    if point.getDistanceFromOrigin() <= 1:
        correctTests += 1
        
print(f"The pi is {4 * (correctTests / totalTests)}")
