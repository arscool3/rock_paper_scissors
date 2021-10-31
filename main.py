import time

import pygame
import random

WIDTH = 1000
HEIGHT = 500
FPS = 30

#Инициализация

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors")
clock = pygame.time.Clock()

#Создание цветов

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Создание сущностей

#кнопка

button = pygame.image.load('button.jpg')
buttonrect = button.get_rect()

#текст

font = pygame.font.SysFont('serif', 50)
user_text  = font.render('Вы выиграли', True,  GREEN)
bot_text = font.render('Вы проиграли', True, RED)
tie_text = font.render('Ничья', True, BLUE)

#бумага

paper_img = pygame.image.load('paper.jpg')
paper = pygame.transform.scale(paper_img, (220, 220))
paperrect = paper.get_rect()

paper_dubl = pygame.transform.scale(paper_img, (220, 220))
paperrect_dubl = paper_dubl.get_rect()

#камень

rock_img = pygame.image.load('rock.jpg')
rock = pygame.transform.scale(rock_img, (220, 220))
rockrect = rock.get_rect()

rock_dubl = pygame.transform.scale(rock_img, (220, 220))
rockrect_dubl = rock_dubl.get_rect()

#ножницы

scissors_img = pygame.image.load('scissors2.jpg')
scissors = pygame.transform.scale(scissors_img, (220, 220))
scissorsrect = scissors.get_rect()

scissors_dubl = pygame.transform.scale(scissors_img, (220, 220))
scissorsrect_dubl = scissors_dubl.get_rect()

#результат

def game(user_choice, bot_choice) :
    running = True
    while running :

        clock.tick(FPS)
        screen.fill(WHITE)

        #цикл событий

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 and 424 <= event.pos[0] <= 600 and 200 <= event.pos[1] <= 244 :
                    running = False

        #отрисовка результата

        if user_choice == bot_choice - 1 or user_choice == bot_choice + 2:
            screen.blit(user_text, (357.5, 50))
        elif user_choice == bot_choice :
            screen.blit(tie_text, (433, 50))
        else :
            screen.blit(bot_text, (348, 50))


        #отрисовка (default)

        buttonrect.x = 424
        buttonrect.y = 200
        screen.blit(button, buttonrect)
        if user_choice == 1 :
            paperrect.x = 180
            screen.blit(paper, paperrect)
        if user_choice == 2 :
            rockrect.x = 180
            screen.blit(rock, rockrect)
        if user_choice == 3 :
            scissorsrect.x = 180
            screen.blit(scissors, scissorsrect)
        if bot_choice == 1 :
            paperrect_dubl.x = 600
            screen.blit(paper_dubl, paperrect_dubl)
        if bot_choice == 2:
            rockrect_dubl.x = 600
            screen.blit(rock_dubl, rockrect_dubl)
        if bot_choice == 3 :
            scissorsrect_dubl.x = 600
            screen.blit(scissors_dubl, scissorsrect_dubl)
        pygame.display.flip()


# Начало игры

running = True
while running :

    #позиционирование обьектов

    paperrect.x = 85
    paperrect.y = 140
    rockrect.x = 390
    rockrect.y = 130
    scissorsrect.x = 695
    scissorsrect.y = 140

    paperrect_dubl.y = 140
    rockrect_dubl.y = 130
    scissorsrect_dubl.y = 140

    #цикл событий

    clock.tick(FPS)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1 :
                if 85 <= event.pos[0] <= 305 and 140 <= event.pos[1] <= 360 :
                    #paper.set_alpha(100)
                    game(1, random.randint(1, 3))
                if 390 <= event.pos[0] <= 610 and 140 <= event.pos[1] <= 360:
                    #rock.set_alpha(100)
                    game(2, random.randint(1, 3))
                if 695 <= event.pos[0] <= 915 and 140 <= event.pos[1] <= 360:
                    #scissors.set_alpha(100)
                    game(3, random.randint(1, 3))

    #отрисовка

    screen.fill(WHITE)
    screen.blit(paper, paperrect)
    screen.blit(rock, rockrect)
    screen.blit(scissors, scissorsrect)
    pygame.display.flip()

pygame.quit()