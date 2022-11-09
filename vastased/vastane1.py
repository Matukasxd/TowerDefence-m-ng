import pygame
import os
from .vastane import vastane
class vastane1(vastane):
    img = []
    for x in range (20):
        add_str = str(x)
        if x < 10:
            add_str = "0" + add_str
        img.append(pygame.image.load(os.path.join("Assets\Jalutab", "1_enemies_1_walk_0" + add_str + ".png")))
    