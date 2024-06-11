from turtle import *
from random import *

class Sprite(Turtle):

    def __init__(self, x, y,step, shape1, color1):
        Turtle.__init__(self)
        self.penup()
        self.speed(5)
        self.goto(x, y)
        self.shape(shape1)
        self.color(color1)
        self.step = step
        self.points = 0
        
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    
    def collid(self, enemy,):
        if self.distance(enemy.xcor(), enemy.ycor()) <= 22:
            return True
        else:
            return False
    
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))
    
    def step_move(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_start, self.y_start, self.x_end, self.y_end)
        
    def step_random(self):
        self.goto(randint(-200, 200), randint(-200, 200))


player = Sprite(0, -100, 10, "turtle", "green")
enemy1 = Sprite(-200, 50, 25, "square", "red")    
enemy2 = Sprite(200, 50, 25, "square", "red")
enemy3 = Sprite(-150, 25, 25, "square", "red")
enemy4 = Sprite(0, 0 , 25, "square", "red")
enemy1.set_move(-200, 75, 200, 75)
enemy2.set_move(200, -25, -200, -25)
enemy3.set_move(150, 25, -150, 25)
enemy4.step_random()
objective = Sprite(0, 150, 10, "triangle", "orange")

scr = player.getscreen()
scr.listen()

scr.onkey(player.move_down, "Down")
scr.onkey(player.move_up, "Up")
scr.onkey(player.move_left, "Left")
scr.onkey(player.move_right, "Right")

while player.points < 3:

    enemy1.step_move()
    enemy2.step_move()
    enemy3.step_move()
    enemy4.step_random()

    if player.collid(objective):
        print("Ваш счет:", player.points + 1)
        player.points += 1
        player.goto(0, -100)

    if player.collid(enemy1):
        print("Ты убит*_*")
        player.goto(0, -100)
        player.points -= 1

    if player.collid(enemy2):
        print("Ты убит*_*")
        player.goto(0, -100)
        player.points -= 1
    
    if player.collid(enemy3):
        print("Ты убит*_*")
        player.goto(0, -100)
        player.points -= 1
    
    if player.collid(enemy4):
        print("Ты убит*_*")
        player.goto(0, -100)
        player.points == 0 

if player.points >= 3 :
    print("ПОБЕДА!!!")
    while 1:
        player.left(360)









