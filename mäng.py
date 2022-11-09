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
kõrgus = 1056
aken = pygame.display.set_mode((laius,kõrgus))
#max framerate, prolly tasub cappida olenevalt display refresist
FPS = 144
WHITE = (255,255,255)
tankix = 100
tankiy = 100
#teeb backgroundi valgeks, seda ei peaks tegelt nkn näha olema
background = pygame.image.load(os.path.join("Assets", "MAP1.png"))
Tank = pygame.image.load(os.path.join("Assets\Tower Tank\PNG\Hulls_Color_A", "Hull_01.PNG"))
Tank = pygame.transform.rotate(pygame.transform.scale(Tank,(tankix,tankiy)), 25)
Tankturret = pygame.image.load(os.path.join("Assets\Tower Tank\PNG\Weapon_Color_A", "Gun_01.PNG"))
Tankturret = pygame.transform.rotate(pygame.transform.scale(Tankturret,(60,75)), 45)

x, y, dx, dy = 360,240,0,0
tankX,tankY= 1500,1200

def mouse(hiir_x, hiir_y):
    global x,y,dx,dy
    dx = hiir_x - x
    dy = hiir_y - y


def display():
    pygame.display.update()
    aken.blit(background, (0,0))
    aken.blit(Tank,(1080,690))
    aken.blit(Tankturret,(1087,705))
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
