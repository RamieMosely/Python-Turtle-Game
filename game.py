import turtle

#Setup Screen
wn = turtle.Screen()
wn.bgcolor("black")


#Create playr turtle
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)

#Create border
myPen = turtle.Turtle()
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

#Set keyboard bindings
turtle.listen()
turtle.onkeypress(turnLeft, "Left")
turtle.onkeypress(turnRight, "Right")
turtle.onkeypress(increaseSpeed, "Up")
turtle.onkeypress(decreaseSpeed, "Down")


while True:
    player.forward(speed)

    #Boundry Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    elif player.ycor() > 300 or player.ycor() < -300:
        player.right(180)







delay = input("Please Enter to quit!")