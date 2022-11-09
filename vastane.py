import pygame

class vastane:
    def __init__(self, laius, kõrgus):
        self.laius = laius
        self.kõrgus = kõrgus
        self.elud = 1
        self.teekond = []
        self.pilt = []
        self.mitmespilt = 0

    def pildile(self, aken):

        self.mitmespilt +=1
        self.pilt = self.imgs[self.mitmespilt]
        aken.blit(self.pilt, (self.laius, self.kõrgus))
        if self.mitmespilt >= len(self.pilt)
        self.liiguta()
    def liiguta(self):
