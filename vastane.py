import pygame

class vastane:
    def __init__(self, laius, kõrgus):
        self.laius = laius
        self.kõrgus = kõrgus
        self.elud = 1
        self.teekond = [(486, 4),(484, 128),(436, 225),(353, 220),(287, 178),(163, 270),(159, 347),(270, 478),(276, 901),(643, 910),(868, 678),(880, 120),(1202, 107),(1299, 18),(1426, 14),(1547, 139),(1552, 212),(1393, 373),(1327, 521),(1296, 643),(1327, 685),(1424, 658),(1520, 713),(1516, 980)]
        self.pilt = []
        self.mitmespilt = 0

    def pildile(self, aken):

        self.mitmespilt +=1
        self.pilt = self.imgs[self.mitmespilt]
        aken.blit(self.pilt, (self.laius, self.kõrgus))
        if self.mitmespilt >= len(self.pilt)
        self.liiguta()
    def liiguta(self):
