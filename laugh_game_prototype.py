import pygame
pygame.init()
from random import randint

back = (153, 204, 255)
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Игра смеха")

clock = pygame.time.Clock()

class TextArea():
    def __init__(self, x, y, width, height, back_color, text, font_size, text_color):
        self.square = pygame.Rect(x, y, width, height)
        self.back_color = back_color
        self.text = text
        self.font_size = font_size
        self.text_color = text_color

    def draw(self):
        shrift = pygame.font.SysFont("Arial", self.font_size)
        text = shrift.render(self.text, True, self.text_color)
        pygame.draw.rect(window, self.back_color, self.square)
        window.blit(text, (self.square.x + 15, self.square.y + 15))

card_question = TextArea(100, 100, 750, 150, (0, 0, 255), "ВОПРОС", 40, (0, 0, 0))
card_answer = TextArea(100, 300, 750, 150, (0, 0, 255), "ОТВЕТ", 40, (0, 0, 0)) 

game_start = True

while game_start == True:
    window.fill(back)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_start = False

            if event.key == pygame.K_q:
                    question_fg = randint(1, 5)
                    if question_fg == 1:
                        card_question.text = "Приветствую, как дела у игрока?"
                    if question_fg == 2:
                        card_question.text = "Сколько собак у краба на облаке?"
                    if question_fg == 3:
                        card_question.text = "Шутка ещё строится, подождите немножко."
                    if question_fg == 4:
                        card_question.text = "Что сказал немой когда парализованный двинулся?"
                    if question_fg == 5:
                        card_question.text = "Сколько пальцев у жителя чернобыля? Я вот тоже не считал."
                
            if event.key == pygame.K_a:
                    answer_rnd = randint(1, 5)
                    if answer_rnd == 1:
                        card_answer.text = "Петя"
                    if answer_rnd == 2:
                        card_answer.text = "50"
                    if answer_rnd == 3:
                        card_answer.text = "Чё надо?"
                    if answer_rnd == 4:
                        card_answer.text = "Где я?"
                    if answer_rnd == 5:
                        card_answer.text = "Что делать если друга сбила машина? Перестать дружить с ним потому что настоящие друзья на дороге не валяются."

    card_question.draw()
    card_answer.draw()

    pygame.display.flip()
    clock.tick(60)