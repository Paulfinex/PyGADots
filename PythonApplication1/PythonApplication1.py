from graphics import *
from random import *
from random import randint
from math import *
import keyboard  
import time
from multiprocessing import Pool
#________________________________________________________________

def windowSetup(width,length):
    window = GraphWin("Genetic Algorithm",width,length)
    window.setBackground("white")
    return window

#________________________________________________________________

def createCircle(startX,startY):
    pt=Point(startX,startY)
    cir=Circle(pt, 4)
    cir.setFill("red")
    return cir

#________________________________________________________________

def twoPointDistance(dot1,dot2):
    x1=dot1.shape.getCenter().getX()
    x2=dot2.shape.getCenter().getX()
    y1=dot1.shape.getCenter().getY()
    y2=dot2.shape.getCenter().getY()
    dist=sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    return round(dist,4)
#________________________________________________________________

class Dot():
    stepNum=0
    reachedGoal=False
    champ=False
    stepList=[]
    alive=True
    collided=False
    fitness=0
    """Dot, individual of the population"""
    def __init__(self,shape,ID):
        self.shape=shape
        self.ID=ID
    def addStep(self,move):
         self.stepList.append(move)

    def Die(self):
        self.alive=False

    def Collide(self):
        self.collided=True



#________________________________________________________________

def Populate(popNum,cirList):
    for count in range(0,popNum):  
        cir=createCircle(250,400)
        x=Dot(cir,"Individual_"+str(count+1))
        cirList.append(x)
    for c in cirList:
        c.shape.draw(win)
    for c in cirList:
        c.stepList =[]
        for i in range(0,maxSteps):
            rStep=randomStep()            
            c.addStep(rStep)
    return cirList

#________________________________________________________________

def Fitness(dot,goal):
    steps=dot.stepNum
    dist=twoPointDistance(dot,goal)
    if(dist<goal.shape.getRadius()):
            
            dot.fitness = sqrt(10000/(steps*steps))
            if(dot.collided):
                dot.fitness=0.1
            return dot
        
    #dot.fitness=1/(dist*dist)
    dot.fitness=sqrt(1/(dist*dist))
    return dot
    
#________________________________________________________________

class gaGeneration():
    genNum=0
    prevGenChampion=None
    freshStart=True

    def __init__(self,ID):
        self.ID=ID
    def nextGen():
        self.genNum+=1
        freshStart=True
    def newChampion(dot):
        prevGenChampion=dot


#________________________________________________________________    


def randomStep():
    step=[]
    stepdist=randint(10,10)
    choice=randint(0,4)
    if(choice == 0):
            step=[0,-stepdist]
    if(choice == 1):
            step=[stepdist,0]
    if(choice == 2):
            step=[-stepdist,0]
    if(choice == 3):
            step=[stepdist,-stepdist]
    if(choice == 4):
            step=[-stepdist,-stepdist]
    if(choice == 5):
            step=[-stepdist,stepdist]
    if(choice == 6):
            step=[stepdist,stepdist]
    if(choice == 7):
            step=[0,stepdist]
    if(choice == 8):
            step=[-stepdist,0]

    return step
 
#________________________________________________________________
def Selection(popList):
    fitSum=0
    bestFit=0
    bestDot=None
    for dot in popList:
        fitSum+=dot.fitness
        if(dot.fitness>bestFit):
            bestFit=dot.fitness
            bestDot=dot
    randVal=uniform(0,fitSum)
    for dot in popList:
        if(dot.fitness>=randVal):
            generation.prevGenChampion=dot
            #dot.shape.setFill("green")
            dot.champ=True
            return dot
    bestDot.champ=True
    generation.prevGenChampion=bestDot
   # print("Error in selection()")
    return bestDot


#________________________________________________________________

def Breeding(dotChamp,popList):
    for dot in popList:
        if(dot.champ==False and dot.reachedGoal==False):
            for i in range(0,maxSteps):
                randChoice=randint(0,6)
                if(randChoice==5 or dot.collided):
                    randChoice=randint(0,1)
                    if(dot.collided and randChoice == 1):
                        dot.stepList[i]=randomStep()
                    if(randChoice == 0 ):
                            dot.stepList[i]=randomStep()
                randChoice=randint(0,2)
                if(randChoice>=1):
                    dot.stepList[i]=dotChamp.stepList[i]
                

        #if(dot.champ==False and dot.reachedGoal==False):
             #for i in range(0,maxSteps):
              #  randChoice=randint(0,40)
               # if(randChoice==1):
                   # dot.stepList[i]=randomStep()
    return Mutate(popList)

#________________________________________________________________

def Mutate(popList):
    for dot in popList:
       if(dot.champ==False):
            randChoice=uniform(0,100)
            if(randChoice<=mutRate):
               # print(dot.ID+" Mutated")
                for i in range(0,maxSteps):
                    dot.stepList[i]=randomStep()
      
    return popList
#________________________________________________________________

def newGeneration(newPopList):
    popList=newPopList
    for dot in popList:
        dot.alive=True
        dot.shape.undraw()
        dot.shape=createCircle(250,400)
        if(dot.reachedGoal ==True):
            dot.shape.setFill("aqua")
        if(dot.champ==True):
            if(dot.reachedGoal==False):
                temp=round(dot.fitness,5)*1000
                prevBestFitText.setText(dot.ID+" fitness Score: "+str(temp))
            if(dot.reachedGoal==True):
                prevBestFitText.undraw()
                prevBestStepText.setText(dot.ID+" reached the Goal in: " + str(dot.stepNum)+" steps.") 
            dot.shape.setFill("lime")
            dot.champ=False
        dot.reachedGoal=False
        dot.stepNum=0
    for dot in popList:
        dot.shape.draw(win)
    generation.genNum+=1
    updateInterface()
    return popList

#________________________________________________________________
def updateInterface():
    textCurrGen.setText("Current Generation: " + str(generation.genNum)+"/"+str(maxGen) +" - Step "+str(popList[1].stepNum)+"/"+str(maxSteps) )
    prevBestDotText.setText("Previous Gen Best: "+ generation.prevGenChampion.ID)
    
#________________________________________________________________

def update(c):
    if(c.alive==True):
        if(twoPointDistance(c,goalDot)<=goalDot.shape.getRadius()):
            c=Fitness(c,goalDot)
            c.reachedGoal=True
            return
        if(c.stepNum>=maxSteps-1):
            c=Fitness(c,goalDot)
            return
        cir=c.shape
       # print(c.stepNum)
        step=c.stepList[c.stepNum]
        c.stepNum+=1
        cir.move(step[0],step[1])
        rad=cir.getRadius()
        cent=cir.getCenter().getY()


        if (((cir.getCenter().getY()<rpt2.getY()+rad)and(cir.getCenter().getY()>rpt1.getY()-rad)) and ((cir.getCenter().getX()<rpt2.getX()+rad)and(cir.getCenter().getX()>rpt1.getX()-rad) )):
            c=Fitness(c,goalDot)
            c.fitness*=0.1
           # print(c.ID+" is dead.")
           # print(c.ID+ "Fitness:"+str(c.fitness))
            c.Collide()
            c.Die()
        if((cir.getCenter().getX()<=0)or(cir.getCenter().getX()>=500)or(cir.getCenter().getY()<=0)or(cir.getCenter().getY()>=500)):
            c=Fitness(c,goalDot)
            c.fitness*=0.01
           # print(c.ID+" is dead.")
           # print(c.ID+ "Fitness:"+str(c.fitness))
            c.Collide()
            c.Die()


maxSteps=50
maxGen=1000
maxPop=100
mutRate=2
win=windowSetup(1000,500)
rpt1=Point(100,220)
rpt2=Point(300,240)
rect = Rectangle(rpt1,rpt2)
rect.setFill("blue")
rect.draw(win)
goalPt=Point(250,40)
goal=Circle(goalPt,10)
goal.setFill("yellow")
goalDot=Dot(goal,"goal")
goal.draw(win)
popList = []
popList=Populate(maxPop,popList)
generation=gaGeneration("gen")
prevBestDot=None
##Interface_________________________________________________
borderP1=Point(500,0)
borderP2=Point(500,500)
border=Rectangle(borderP1,borderP2)
border.setFill("black")
border.draw(win)
genString="Current Generation: " + str(generation.genNum)
textCurrGen = Text(Point(750,50), genString)
textCurrGen.draw(win)
prevBestDotString=""
prevBestDotText = Text(Point(750,75), prevBestDotString)
prevBestDotText.draw(win)
prevBestFitString=""
prevBestFitText = Text(Point(750,100), prevBestFitString)
prevBestFitText.draw(win)
prevBestStepString=""
prevBestStepText = Text(Point(750,100), prevBestStepString)
prevBestStepText.draw(win)
#___________________________________________________________




while(generation.genNum<maxGen):

    for i in range (0,maxSteps):
        
        textCurrGen.setText("Current Generation: " + str(generation.genNum)+"/"+str(maxGen) +" - Step "+str(i+1)+"/"+str(maxSteps) )
        for c in popList:
           update(c)
            #time.sleep(0.0015)
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):
                win.close()
            if keyboard.is_pressed('p'): 
                break        
        except:
            break  # if user pressed a key other than the given key the loop will break
    popList=newGeneration(Breeding(Selection(popList),popList))
    


win.getMouse()
win.close()


