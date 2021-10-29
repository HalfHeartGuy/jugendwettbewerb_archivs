
import turtle
from turtle import *
from random import randint

screen = turtle.getscreen()
screen.clear()
screen.title("Game")
myTurtle = turtle.Turtle()
myTurtle.reset()

def colors():
    colors = []
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colors.append(r,g,b)
    return colors




def rechteck(laenge,breite):

    for i in range(0,2):
        myTurtle.forward(laenge)
        myTurtle.right(90)
        myTurtle.forward(breite)
        myTurtle.right(90)



def positionieren(abstand):

    myTurtle.forward(abstand)
    myTurtle.right(90)
    myTurtle.forward(abstand)
    myTurtle.left(90)







def außen_rechteck_zeichner(laenge,breite,abstand):


    #rechteck zeichnen
    pencolor = colors()
    myTurtle.pencolor("green")
    myTurtle.pendown()

    rechteck(laenge,breite)
    myTurtle.penup()
    myTurtlePos = zweite_schicht((laenge - abstand * 3) / 2,breite - abstand * 2,abstand)
#    laenge = (laenge - abstand * 3) / 2
 #   breite = breite - abstand * 2
    rechteck_schoner((laenge - abstand * 3) / 2,breite - abstand * 2,abstand,myTurtlePos[0],myTurtlePos[1])

def zweite_schicht(laenge,breite,abstand):


    #positioneiren zweite schicht
    myTurtle.penup()
    positionieren(abstand)
    myTurtle.pendown()

    #rechteck zeichnen
    rechteck(laenge,breite)


    #positionieren rechten rechteck

    myTurtle.penup()
    myTurtle.forward(laenge + abstand)
    myTurtle.pendown()


    #rechteck zeichnen

    rechteck(laenge,breite)

    #positieren zurück zur linken Rechteck

    myTurtle.penup()
    myTurtle.back(laenge + abstand)

    myTurtlePos = myTurtle.pos()
    return myTurtlePos
def rechteck_schoner(laenge,breite,abstand,x,y):

    if laenge > abstand * 2:
        zweite_schicht((laenge - abstand * 3) / 2, breite - abstand * 2, abstand)
        rechteck_schoner((laenge - abstand * 3) / 2, breite - abstand * 2, abstand, x + abstand , y - abstand)
    #positienieren
    myTurtle.penup()
    myTurtle.goto(x,y)
    myTurtle.forward(laenge + abstand)

    #rekursion rechts

    if laenge > abstand * 2:
        myTurtlePos = myTurtle.pos()

        x = myTurtlePos[0]
        y = myTurtlePos[1]
        zweite_schicht((laenge - abstand * 3) / 2, breite - abstand * 2, abstand)
        rechteck_schoner((laenge - abstand * 3) / 2, breite - abstand * 2, abstand, x + abstand, y - abstand)






außen_rechteck_zeichner(500,250,20)


