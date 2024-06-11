from turtle import *

window = Screen()
window.bgcolor("#8095FF")
window.title("Серце))")

def heart():

    speed(0)
    color("#E60000")
    begin_fill()

    up()
    goto(0,0)
    down()

    left(140)
    forward(224)

    # Основна петля малювання серця
    for i in range(200):
        speed(0)
        right(1)
        forward(2)

    # Закінчення малювання серця
    left(120)
    for j in range(200):
        speed(0)
        right(1)
        forward(2)

    forward(224)
    end_fill()
    hideturtle()

heart()
exitonclick()