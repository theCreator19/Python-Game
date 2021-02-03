import pygame,random,sys
from pygame.locals import *
pygame.init()
sc_w=500
sc_h=500
screen = pygame.display.set_mode((sc_w,sc_h))
pygame.display.set_caption("My game")


def man():
    x = 487
    y = 5
    wid = 10
    ht = 100
    vel = 5
    x2 = 5
    y2 = 5
    run = True
    while run:
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and y>vel:
            y -= vel
        if keys[pygame.K_DOWN] and y<sc_h-ht-vel:
            y += vel
        if keys[pygame.K_w] and y2>vel:
            y2 -= vel
        if keys[pygame.K_s] and y2<sc_h-ht-vel:
            y2 += vel

        screen.fill((130, 132, 176))
        pygame.draw.line(screen, (22, 22, 22), (250, 0), (250, 500))
        pygame.draw.rect(screen, (0, 0, 255), (2.5, 2.5, 497.5, 497.5), 4)
        pygame.draw.rect(screen, (255, 0, 0), (x, y, wid, ht))

        pygame.draw.rect(screen, (0, 255, 0), (x2, y2, wid, ht))
        pygame.draw.circle(screen, (222, 120, 150), (250, 250), 10)

        basic_font = pygame.font.Font('freesansbold.ttf', 20)
        player_text = basic_font.render(f"My score : ", False, (200,23,242))
        screen.blit(player_text, (290, 20))

        opponent_text = basic_font.render(f"Oppanent's score : ", False, (200,22,223))
        Aman_text = basic_font.render(f"By Aman Agarwal  ", False, (50, 25, 22))
        screen.blit(opponent_text, (290, 50))
        screen.blit(Aman_text, (290, 400))

        pygame.display.update()

man()
pygame.quit()