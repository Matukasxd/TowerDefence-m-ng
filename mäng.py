import pygame
laius = 1920
kõrgus = 1080
win = pygame.display.set_mode((laius,kõrgus))
FPS = 144
WHITE = (255,255,255)
def display():
    win.fill(WHITE)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        display()
    pygame.quit()
main()
