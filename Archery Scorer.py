import math

from graphics import *


def inCircle(pt1, circ):
    dx = pt1.getX() - circ.getCenter().getX()
    dy = pt1.getY() - circ.getCenter().getY()
    dist = math.sqrt(dx * dx + dy * dy)
    
    return dist <= circ.getRadius()
    
def main():
    win = GraphWin("Archery Board" , 1000 , 1000)
    one = Circle(Point(500 , 500) , 375)
    three = Circle(Point(500 , 500) , 300)
    five = Circle(Point(500 , 500) , 225)
    seven = Circle(Point(500 , 500) , 150)
    nine = Circle(Point(500 , 500) , 75)
    
    one.setFill("white")
    three.setFill("black")
    five.setFill("blue")
    seven.setFill("red")
    nine.setFill("yellow")
    
    one.draw(win)
    three.draw(win)
    five.draw(win)
    seven.draw(win)
    nine.draw(win)
    
    score = 0
    totalScore = 0
    for i in range(5):
        click = win.getMouse()

        if inCircle(click , nine):
            score = 9
            
        elif inCircle(click , seven):
            score = 7
            
        elif inCircle(click , five):
            score = 5
            
        elif inCircle(click , three):
            score = 3
            
        elif inCircle(click , one):
            score = 1
            
        print("That click was worth" , score , "points")
        totalScore += score
        
    print("Your total score was" , totalScore)

main()
