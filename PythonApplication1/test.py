from graphics import *
from math import *
from random import *
win = GraphWin("window",1000,500)
win.setBackground("white")

def createCircle(startX,startY):
    pt=Point(startX,startY)
    cir=Circle(pt, 5)
    cir.setFill("red")
    return cir
class Dot():
    
    stepList=[]
    alive=True
    fitness=1
    """Dot, individual of the population"""
    def __init__(self,shape,ID):
        self.shape=shape
        self.ID=ID

    def addStep(self,move):
        stepList.attach(move)

    def Die(self):
        self.alive=False

def twoPointDistance(dot1,dot2):
    x1=dot1.shape.getCenter().getX()
    x2=dot2.shape.getCenter().getX()
    y1=dot1.shape.getCenter().getY()
    y2=dot2.shape.getCenter().getY()
    dist=sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    return round(dist,4)
list=[1,2,3,4,5]
print(len(list))
cir=createCircle(249,448)
cir2=createCircle(250,450)
dot1=Dot(cir,"circle"+str(1))
dot2=Dot(cir2,"circle"+str(2))
dot1.shape.draw(win)
dot2.shape.draw(win)
dot1.shape.getRadius()
dot1.shape.getCenter().getX()
dist=twoPointDistance(dot1,dot2)
print(randrange(10))
print("__________"+str(1/(dist*dist)))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
print("Fitness:" + str(uniform(0,(1/(dist*dist)))))
dot1.shape.x=10
dot1.shape.y=10

dot1.shape.undraw()
win.getMouse()
win.close()

dot1.shape.color
def randomStep():
    step=[]
    choice=randint(0,7)
    if(choice == 0):
            step=[0,5]
    if(choice == 1):
            step=[0,-5]
    if(choice == 2):
            step=[5,5]
    if(choice == 3):
            step=[5,-5]
    if(choice == 4):
            step=[-5,5]
    if(choice == 5):
            step=[-5,-5]
    if(choice == 6):
            step=[5,0]
    if(choice == 7):
            step=[-5,0]
    return step

while True:
    print(randomStep())
    time.sleep(0.5)