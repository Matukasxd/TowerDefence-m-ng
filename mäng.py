import pygame
import math
import os
#TODO:
#turretite valik, mäng vaatab kus on hiire positsioon kui on turreti valikus mingi torni peal,
#ja tuleb
#turreteid saab asetada erinevates suunades, nt kui kontrollid torni ja vajutad R tähte
#siis saad torni asukohta muuta
#eventidega vaatama, kas hiirega vajutatakse torni valikute peale või asetatakse mapi peale
#reso
laius = 1920
kõrgus = 1080
aken = pygame.display.set_mode((laius,kõrgus))
#max framerate, prolly tasub cappida olenevalt display refresist
FPS = 144
WHITE = (255,255,255)
#teeb backgroundi valgeks, seda ei peaks tegelt nkn näha olema
background = pygame.image.load(os.path.join("Assets", "MAP1.png"))
x, y, dx, dy = 360,240,0,0
def mouse(hiir_x, hiir_y):
    global x,y,dx,dy
    dx = hiir_x - x
    dy = hiir_y - y


def display():
    pygame.display.update()
    aken.blit(background, (0,0))

def main():
    uuenda = False
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(1)
    run = True #laseb päriselt akna sulgeda
    while run:
        clock.tick(FPS) #määrab FPSi mängu tickrateks?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            hiir = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(hiir)
        if uuenda:
            mouse(hiir_x,hiir_y)
        display()
    pygame.quit()
main()
