from turtle import *
from PIL import Image
import pygame as pg
from pygame import mixer

window = Screen()
window.bgcolor("#8095FF")
window.title("ДЛЯ ЗІРОНЬКИ💕")
window.setup(width=1.0, height=1.0)
pg.init()
#...
mixer.music.load("...")
mixer.music.play(-1)
try:
    def heart():
        speed(0)
        color("#E60000")
        begin_fill()
        up()
        goto(0,0)
        down()
        left(140)
        forward(224)
        speed(0)
        for i in range(200):
            speed(0)
            right(1)
            forward(2)
        speed(0)
        left(120)
        for j in range(200):
            speed(0)
            right(1)
            forward(2)
        forward(224)
        end_fill()
        hideturtle()
        up()
except:
    pass
def love():
    # БУКВА Я
    showturtle()
    goto(-550,-180)
    down()
    left(50)
    right(180)
    right(90)
    begin_fill()
    right(135)
    forward(108)
    left(135)
    right(180)
    forward(20)
    right(135)
    forward(108)
    end_fill()
    right(48)
    forward(20)
    right(87)
    begin_fill()
    forward(82)
    left(90)
    forward(25)
    left(90)
    forward(167)
    left(90)
    forward(25)
    left(90)
    forward(92)
    end_fill()
    showturtle()
    left(180)
    forward(21)
    left(90)
    begin_fill()
    forward(25)
    for i in range(22):
        right(8)
        forward(4)
        
    right(3)
    forward(25)
    left(90)
    forward(12)
    left(89)
    forward(50)
    for i in range(25):
        left(7)
        forward(5)
    left(5)
    forward(49)
    end_fill()
    up()
    forward(120)
    down()
    # Буква Т
    begin_fill()
    right(90)
    forward(79)
    left(90)
    forward(25)
    left(90)
    forward(140)
    right(90)
    forward(50)
    left(90)
    forward(24)
    left(90)
    forward(130)
    left(90)
    forward(24)
    left(90)
    forward(55)
    right(90)
    forward(76)
    end_fill()
    
    # буква Е
    up()
    left(90)
    forward(115)
    right(90)
    forward(60)
    down()
    begin_fill()
    left(90)
    forward(25)
    left(90)
    forward(160)
    left(90)
    forward(25)
    left(90)
    forward(160)
    left(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(100)
    end_fill()
    # Буква Б
    up()
    right(180)
    forward(140)
    down()
    begin_fill()
    right(90)
    forward(160)
    left(90)
    forward(25)
    left(90)
    forward(160)
    left(90)
    forward(25)
    end_fill()
    begin_fill()
    right(180)
    forward(85)
    right(90)
    forward(20)
    right(90)
    forward(85)
    right(90)
    end_fill()
    forward(20)
    left(180)
    forward(45)
    left(90)
    up()
    forward(25)
    down()
    color("#E60000")
    begin_fill()
    for i in range(37):
        forward(5)
        right(5)
    end_fill()
    right(85)
    forward(95)
    right(90)
    begin_fill()
    color("#8095FF")
    circle(-40,180)
    end_fill()
    # Буква е
    up()
    right(180)
    forward(100)
    right(90)
    forward(17)
    left(90)
    down()
    color("#E60000")
    right(90)
    begin_fill()
    left(90)
    forward(25)
    left(90)
    forward(160)
    left(90)
    forward(25)
    left(90)
    forward(160)
    left(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    left(90)
    forward(20)
    left(90)
    forward(100)
    end_fill()
    # Буква Л
    up()
    right(180)
    forward(150)
    down()
    begin_fill()
    right(90)
    forward(165)
    left(90)
    forward(25)
    left(90)
    forward(165)
    left(90)
    forward(25)
    end_fill()
    begin_fill()
    right(180)
    forward(100)
    right(90)
    forward(20)
    right(90)
    forward(100)
    end_fill()
    begin_fill()
    right(180)
    forward(75)
    right(90)
    forward(145)
    left(90)
    forward(25)
    left(90)
    forward(145)
    end_fill()
    begin_fill()
    right(180)
    forward(145)
    left(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(25)
    end_fill()
    # Буква Ю
    up()
    right(180)
    forward(60)
    down()
    begin_fill()
    right(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(165)
    left(90)
    forward(25)
    left(90)
    forward(145)
    end_fill()
    
    left(90)
    up()
    forward(25)
    left(90)
    forward(50)
    begin_fill()
    right(90)
    down()
    forward(35)
    left(90)
    forward(20)
    left(90)
    forward(35)
    right(180)
    end_fill()
    forward(20)
    right(45)
    up()
    forward(120)
    down()
    begin_fill()
    left(90)  # Початковий кут повороту
    for _ in range(2):
        circle(105, 90)  # Радіуси відповідають пропорціям овала
        circle(60 / 2, 90)
    end_fill()
    left(45)
    up()
    forward(25)
    left(90)
    forward(5)
    right(90)
    color("#8095FF")
    down()
    right(45)
    begin_fill()
    for _ in range(2):
        circle(67, 90)  # Радіуси відповідають пропорціям овала
        circle(40 / 2, 90)
    end_fill()
    # Буква Б
    up()
    color("#E60000")
    right(45)
    forward(75)
    left(90)
    forward(135)
    right(90)
    down()
    begin_fill()
    right(90)
    forward(165)
    left(90)
    forward(25)
    left(90)
    forward(165)
    left(90)
    forward(25)
    end_fill()
    begin_fill()
    right(180)
    forward(85)
    right(90)
    forward(20)
    right(90)
    forward(85)
    right(90)
    end_fill()
    forward(20)
    left(180)
    forward(50)
    left(90)
    up()
    forward(25)
    down()
    color("#E60000")
    begin_fill()
    for i in range(37):
        forward(5)
        right(5)
    end_fill()
    right(85)
    forward(95)
    right(90)
    begin_fill()
    color("#8095FF")
    circle(-40,180)
    end_fill()
    up()
    color("#E60000")
    right(90)
    forward(148) #146 18
    right(90)
    down()
    up()
    forward(100)
    down()
    # Буква Л
    begin_fill()
    right(90)
    forward(165)
    left(90)
    forward(25)
    left(90)
    forward(165)
    left(90)
    forward(25)
    end_fill()
    begin_fill()
    right(180)
    forward(100)
    right(90)
    forward(20)
    right(90)
    forward(100)
    end_fill()
    begin_fill()
    right(180)
    forward(75)
    right(90)
    forward(145)
    left(90)
    forward(25)
    left(90)
    forward(145)
    end_fill()
    begin_fill()
    right(180)
    forward(145)
    left(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(25)
    end_fill()
    up()
    right(180)
    forward(75)
    down()
# Буква Ю
    begin_fill()
    right(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(165)
    left(90)
    forward(25)
    left(90)
    forward(145)
    end_fill()
    
    left(90)
    up()
    forward(25)
    left(90)
    forward(50)
    begin_fill()
    right(90)
    down()
    forward(35)
    left(90)
    forward(20)
    left(90)
    forward(35)
    right(180)
    end_fill()
    forward(20)
    right(45)
    up()
    forward(120)
    down()
    begin_fill()
    left(90)  # Початковий кут повороту
    for _ in range(2):
        circle(105, 90)  # Радіуси відповідають пропорціям овала
        circle(60 / 2, 90)
    end_fill()
    left(45)
    up()
    forward(25)
    left(90)
    forward(5)
    right(90)
    color("#8095FF")
    down()
    right(45)
    begin_fill()
    for _ in range(2):
        circle(67, 90)  # Радіуси відповідають пропорціям овала
        circle(40 / 2, 90)
    end_fill()
heart()
love()
path = "C:/Users/alkog/Desktop/folder/python/images/gif_l2.gif"
path2 = "C:/Users/alkog/Desktop/folder/python/images/gif_s.gif"
new_height = 250
new_width = 250
new_height2 = 250
new_width2 = 200
input_file = path
output_file = path
input_file2 = path2
output_file2 = path2
# ----------------------------
image1 = Image.open(input_file2)
resized_image2 = image1.resize((new_width2, new_height2), Image.ANTIALIAS)
resized_image2.save(output_file2)
# Create a turtle for the image
image_turtle2 = Turtle()
register_shape(path2)
image_turtle2.up()
image_turtle2.goto(-400, 150)  
image_turtle2.showturtle()
image_turtle2.shape(path2)
image_turtle2.showturtle()
# ----------------------------
# ----------------------------
image = Image.open(input_file)
resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
resized_image.save(output_file)
# Create a turtle for the image
image_turtle = Turtle()
register_shape(path)
image_turtle.up()
image_turtle.goto(400, 150)  
image_turtle.showturtle()
image_turtle.shape(path)
image_turtle.showturtle()
# ----------------------------
exitonclick()




