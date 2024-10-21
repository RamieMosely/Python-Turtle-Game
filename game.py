import turtle
import math
import random

#Setup Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(2)


#Create playr turtle
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
#player.penup()
player.speed(0)


#Create the score variable
score = 0

#Create multiple goals
maxGoals = 6
goal = []
for count in range(maxGoals):
    goal.append(turtle.Turtle())
    goal[count].color("blue")
    goal[count].shape("circle")
    goal[count].penup()
    goal[count].speed(0)
    goal[count].setposition(random.randint(-300, 300), random.randint(-300, 300))


#Create border
myPen = turtle.Turtle()
myPen.speed(5)
myPen.penup()
myPen.setposition(-300, -300)
myPen.pendown()
myPen.pensize(4)
myPen.color("white")
for side in range(4):
    myPen.forward(600)
    myPen.left(90)
myPen.hideturtle()


#Set speed
speed = 1

def turnLeft():
    player.left(30)

def turnRight():
    player.right(30)

def increaseSpeed():
    global speed
    speed += 1

def decreaseSpeed():
    global speed
    speed -= 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


#Set keyboard bindings
turtle.listen()
turtle.onkeypress(turnLeft, "Left")
turtle.onkeypress(turnRight, "Right")
turtle.onkeypress(increaseSpeed, "Up")
turtle.onkeypress(decreaseSpeed, "Down")


while True:
    player.forward(speed)

    #Boundry Checking
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    elif player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        


    

    



    #Collision Checking
    for count in range(maxGoals):
        goal[count].forward(1)
            #Boundry Checking for goal
        if goal[count].xcor() > 290 or goal[count].xcor() < -290:
            goal[count].right(180)
        elif goal[count].ycor() > 290 or goal[count].ycor() < -290:
            goal[count].right(180)

        if isCollision(player, goal[count]):
            goal[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goal[count].right(random.randint(0, 360))
            score += 1
            #Draw the score
            myPen.undo()
            myPen.penup()
            myPen.hideturtle()
            myPen.setposition(-290, 310)
            scoreString = "Score: %s"%score
            myPen.write(scoreString, False, align ="left", font=("Ariel", 14, "normal"))


            print(score)
   



delay = input("Please Enter to quit!")