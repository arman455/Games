from turtle import *
from time import * 
from random import *
counter = 0
print("Поймай меня если сможешь *-*")

t1 = Turtle()
t1.shape("turtle")
t1.color("green")
t1.penup()

def catch():
    t1.write("Ты меня поймал ;)")
    counter += 1
t1.speed(20)
while True:
    t1.goto(randint(-300, 300), randint(-300, 300))
    t1.onclick(catch)
    if counter == 1:
        print("Ты победил :)")
        break

done()