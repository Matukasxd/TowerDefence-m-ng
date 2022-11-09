import pygame
#reso
laius = 1920
kõrgus = 1080
aken = pygame.display.set_mode((laius,kõrgus))
#max framerate, prolly tasub cappida olenevalt display refresist
FPS = 144
WHITE = (255,255,255)
#teeb backgroundi valgeks, seda ei peaks tegelt nkn näha olema
def display():
    aken.fill(WHITE)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(1)
    run = True #laseb päriselt akna sulgeda
    while run:
        clock.tick(FPS) #määrab FPSi mängu tickrateks?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        display()
    pygame.quit()
main()
