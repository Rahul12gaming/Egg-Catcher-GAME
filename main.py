import time
from pygame import mixer
import pygame
import random

pygame.font.init()
mixer.init()


#screen&&caption
screen=pygame.display.set_mode((955,537))
pygame.display.set_caption("eggcatchet")

#coordinate of basket
basketX=100
basketY=380
basketX_change=0
basket=pygame.image.load('basket (1).png')

bg=pygame.image.load('bgimage.jpeg')

#egg img and coordinate
egg=[
    pygame.image.load('white egg.png')


     ]

number_1=1

eggX=[]

eggY=[]

eggy_change=[]

score=0

mixer.music.load('bgsound.mp3')
mixer.music.play(-1)


font=pygame.font.Font('freesansbold.ttf',32)
game_over=pygame.font.Font('freesansbold.ttf',55)


#passfont=pygame.font.Font('freesansbold.ttf',72)
def over_text(x,y):
    overvalue=game_over.render('game over',True,(0,255,255))
    screen.blit(overvalue,(x,y))

def show_score(x,y):
    score_value=font.render('score: '+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))

#def level(x,y):
   # pass_value=passfont.render("LEVEL 1 IS CLEAR",True,(255,0,255))
    #screen.blit(pass_value,(x,y))

for i in range(number_1):
    eggX.append(random.randint(0,570))
    eggY.append(random.randint(0,100))
    eggy_change.append(1)

def egg_show(x,y,i):
    screen.blit(egg[i],(x,y))
run=True
while run:

    #mixer.music.play(music)
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                basketX_change=-2
            if event.key==pygame.K_RIGHT:
                basketX_change=+2

    for i in range(number_1):
        if eggY[i]>=450:
            eggX[i]=random.randint(0,570)
            eggY[i]=random.randint(0,100)
        eggY[i] += eggy_change[i]
        if eggY[i]<=450:
            egg_show(eggX[i], eggY[i], i)

        if 450 <= eggY[i]:
            over_text(350, 250)
            run=False

        egg_rect=pygame.Rect(eggX[i],eggY[i],32,50)
        rot_rect=pygame.Rect(basketX+40,basketY+30,80,120)
        if egg_rect.colliderect(rot_rect):

            eggX[i]=random.randint(20,480)
            eggY[i]=random.randint(0,100)
            score+=1
            collect=mixer.Sound('rrr.wav')
            collect.play()

    if basketX>=955:
     basketX=955
    if basketX<=0:
        basketX=0



    show_score(20, 20)
    basketX += basketX_change
    screen.blit(basket, (basketX, basketY))
    pygame.display.update()