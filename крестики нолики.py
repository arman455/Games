from turtle import *
check_x_1 = 0
check_o_1 = 0

check_x_2 = 0
check_o_2 = 0

check_x_3 = 0
check_o_3 = 0

check_x_4 = 0
check_o_4 = 0

check_x_5 = 0
check_o_5 = 0

check_x_6 = 0
check_o_6 = 0

check_x_7 = 0
check_o_7 = 0

check_x_8 = 0
check_o_8 = 0

check_x_9 = 0
check_o_9 = 0

speed(0)
penup()
goto(-150, 150)
pendown()
for i in range(4):
    forward(200)
    right(90)
right(90)
forward(65)
left(90)
forward(200)
right(90)
forward(65)        
right(90)
forward(200)
left(90) 
forward(70)
left(90) 
forward(65)
left(90)
forward(200)
right(90)
forward(68)
right(90)
forward(200)
left(180)
speed(100)
b = 0
move = 0
while move <= 9:
    a = int(input("Хто ходит первым?? 1-x  2-0"))
    if a == 1:
        b = int(input("Введи номер позиции:"))
        if b == 1:
            if check_x_1 == 1:
                print("занято)")
            else:
                penup()
                goto(-150, 86)
                pendown()
                color("red")
                right(47)
                forward(92)
                left(180)
                forward(46)
                right(88)
                forward(46)
                left(180)
                forward(92)
                left(135)
                check_x_1 = 1
        if b == 2:
            if check_x_2 == 1:
                print("занято)")
            else:
                penup()
                goto(-84, 86)
                pendown()
                color("red")
                right(47)
                forward(92)
                left(180)
                forward(46)
                right(88)
                forward(46)
                left(180)
                forward(92)
                left(135)
                check_x_2 = 1
                move += 1
        if b == 3:
            if check_x_3 == 1:
                print("занято)")
            else:
                penup()
                goto(-16, 86)
                pendown()
                color("red")
                right(47)
                forward(92)
                left(180)
                forward(46)
                right(88)
                forward(46)
                left(180)
                forward(92)
                left(135)
                check_x_3 = 1
                move += 1
# Вот тут была путаница
        if b == 6:
            if check_x_6 == 1:
                print("занято)")
            else:
                penup()
                goto(-16, 20)
                pendown()
                color("red")
                right(47)
                forward(92)
                left(180)
                forward(46)
                right(88)
                forward(46)
                left(180)
                forward(92)
                left(135)
                check_x_6 = 1
                move += 1
        if b == 5:
            if check_x_5 == 1:
                print("занято)")
            else:
                penup()
                goto(-84, 20)
                pendown()
                color("red")
                right(47)
                forward(92)
                left(180)
                forward(46)
                right(88)
                forward(46)
                left(180)
                forward(92)
                left(135)
                check_x_5 = 1
                move += 1
        if b == 4:
            if check_x_4 == 1:
                print("занято)")
            else:
                penup()
                goto(-150, 20)
                pendown()
                color("red")
                right(47)
                forward(92)
                left(180)
                forward(46)
                right(88)
                forward(46)
                left(180)
                forward(92)
                left(135)
                check_x_4 = 1
                move += 1
        if b == 7:
            if check_x_7 == 1:
                print("занято)")
            else:
                penup()
                goto(-150, -48)
                pendown()
                color("red")
                right(44)
                forward(92)
                left(180)
                forward(46)
                right(94)
                forward(46)
                left(180)
                forward(92)
                left(135)
                check_x_7 = 1
                move += 1
        if b == 8:
            if check_x_8 == 1:
                print("занято)")
            else:
                penup()
                goto(-84, -48)
                pendown()
                color("red")
                right(44)
                forward(93)
                left(180)
                forward(46)
                right(92)
                forward(46)
                left(180)
                forward(93)
                left(135)
                check_x_8 = 1
                move += 1
        if b == 9:
            if check_x_9 == 1:
                print("занято)")
            else:
                penup()
                goto(-16, -48)
                pendown()
                color("red")
                right(44)
                forward(93)
                left(180)
                forward(46)
                right(92)
                forward(46)
                left(180)
                forward(93)
                left(135)
                check_x_9 = 1
                move += 1
    elif a == 2:
        b = int(input("Введи номер позиции:"))
        if b == 1:
            if check_o_1 == 1:
                print("занято)")
            else:
                penup()
                goto(-87, 116)
                pendown()
                color("blue")
                circle(32)
                check_o_1 = 1
                move += 1
        if b == 2:
            if check_o_2 == 1:
                print("занято)")
            else:
                penup()
                goto(-20, 116)
                pendown()
                color("blue")
                circle(32)
                check_o_2 = 1
                move += 1
        if b == 3:
            if check_o_3 == 1:
                print("занято)")
            else:
                penup()
                goto(47, 116)
                pendown()
                color("blue")
                circle(32)
                check_o_3 = 1
                move += 1
        if b == 4:
            if check_o_4 == 1:
                print("занято)")
            else:
                penup()
                goto(-87, 50)
                pendown()
                color("blue")
                circle(32)
                check_o_4 = 1
                move += 1
        if b == 5:
            if check_o_5 == 1:
                print("занято)")
            else:
                penup()
                goto(-20, 50)
                pendown()
                color("blue")
                circle(32)
                check_o_5 = 1
                move += 1
        if b == 6:
            if check_o_6 == 1:
                print("занято)")
            else:
                penup()
                goto(47, 50)
                pendown()
                color("blue")
                circle(32)
                check_o_6 = 1
                move += 1
        if b == 7:
            if check_o_7 == 1:
                print("занято)")
            else:
                penup()
                goto(-87,-17)
                pendown()
                color("blue")
                circle(32)
                check_o_7 = 1
                move += 1
        if b == 8:
            if check_o_8 == 1:
                print("занято)")
            else:
                penup()
                goto(-20, -17)
                pendown()
                color("blue")
                circle(32)
                check_o_8 = 1
                move += 1
        if b == 9:
            if check_o_9 == 1:
                print("занято)")
            else:
                penup()
                goto(47, -17)
                pendown()
                color("blue")
                circle(32)
                check_o_9 = 1
                move += 1
# Здесь елиф заменил на иф. Вроде работает, но не все комбинации проверил
    if check_x_1 == 1 and check_x_2 == 1 and check_x_3 == 1:
        print("Победил крестик:)")
        break
    elif check_o_1 == 1 and check_o_2 == 1 and check_o_3 == 1:
        print("Победил нолик:)")
        break
    elif check_x_4 == 1 and check_x_5 == 1 and check_x_6 == 1:
        print("Победил крестик:)")
        break   
    elif check_o_4 == 1 and check_o_5 == 1 and check_o_6 == 1:
        print("Победил нолик:)")
        break
    elif check_x_7 == 1 and check_x_8 == 1 and check_x_9 == 1:
        print("Победил крестик:)")
        break   
    elif check_o_7 == 1 and check_o_8 == 1 and check_o_9 == 1:
        print("Победил нолик:)")
        break
    elif check_x_1 == 1 and check_x_4 == 1 and check_x_7 == 1:
        print("Победил крестик:)")
        break   
    elif check_o_1 == 1 and check_o_4 == 1 and check_o_7 == 1:
        print("Победил нолик:)")
        break
    elif check_x_2 == 1 and check_x_5 == 1 and check_x_8 == 1:
        print("Победил крестик:)")
        break   
    elif check_o_2 == 1 and check_o_5 == 1 and check_o_8 == 1:
        print("Победил нолик:)")
        break
    elif check_x_3 == 1 and check_x_6 == 1 and check_x_9 == 1:
        print("Победил крестик:)")
        break   
    elif check_o_3 == 1 and check_o_6 == 1 and check_o_9 == 1:
        print("Победил нолик:)")
        break
    elif check_x_1 == 1 and check_x_5 == 1 and check_x_9 == 1:
        print("Победил крестик:)")
        break   
    elif check_o_3 == 1 and check_o_5 == 1 and check_o_7 == 1:
        print("Победил нолик:)")
        break
if move == 10:
    print("Ничья")    
        

exitonclick()
                
