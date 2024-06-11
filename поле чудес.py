from turtle import * 
import os # модуль для работы с операционными системами
os.system('cls') # очищение консоли

word = input("Введите слово, которое хотите загадать: ").upper() # загаданное слово
word_in_list = list(word) # превращаем строку в список
stars = "*" * len(word)
description = input("Введите описание к вашему слову: ") # подсказка к слову

os.system('cls')

print("--------")
print("Игра началась! Попробуйте угадать слово из", len(word), "букв") # len - это функция для поиска длины текста
print(stars)
print("Подсказка к этому слову:", description)
print("--------")

counter = -300
turtles_list = [] # список для всех клеток-черепах

for i in word: # создаем черепах в том количестве, сколько букв в слове
    t = Turtle()
    t.penup()
    t.color("yellow", "blue")
    t.shape("square")
    t.shapesize(5)
    t.goto(counter, 0)
    counter += 100
    turtles_list.append(t) # добавляем черепаху в список

stars = ""

while True:
    letter = input("Угадайте букву: ").upper()
    if letter in word:
        print("Буква найдена! Откройте её!")
        for i in word_in_list: # если буква имеется - раскрываем ее, а остальные спрятаны
            if i == letter:
                stars += letter
            else:
                stars += "*"
        print(stars)
    else:
        print("Буква не найдена! Пробуйте еще раз!")

done()