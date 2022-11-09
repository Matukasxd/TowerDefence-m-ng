import pygame

class vastane:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.elud = 1
        self.asukoht = 0
        self.teekond = [(486, 4),(484, 128),(436, 225),(353, 220),(287, 178),(163, 270),(159, 347),(270, 478),(276, 901),(643, 910),(868, 678),(880, 120),(1202, 107),(1299, 18),(1426, 14),(1547, 139),(1552, 212),(1393, 373),(1327, 521),(1296, 643),(1327, 685),(1424, 658),(1520, 713),(1516, 980)]
        self.pilt = []
        self.mitmespilt = 0
        self.samme = 0
        self.kaugus

    def pildile(self, aken):

        self.mitmespilt +=1
        self.pilt = self.imgs[self.mitmespilt]
        aken.blit(self.pilt, (self.x, self.y))
        if self.mitmespilt >= len(self.pilt):
            self.mitmespilt = 0
        self.liiguta()
    def liiguta(self):
        x1,y1 = self.teekond[self.asukoht]
        if self.asukoht + 1 >= len(self.teekond):
            x2,y2 = (1526, 1070)
        else:
            x2,y2 = self.teekond[self.asukoht + 1]
        liikumine += math.sqrt((x2-x1)**2 + (y2-y1)**2)
        self.samme += 1
        muutx = x2 - x1
        muuty = y2 - y1
        liigux, liiguy = (self.x + muutx * self.samme, self.y + muuty * self.samme)
        self.kaugus += math.sqrt((liigux-x1)**2 + (liiguy-y1)**2)
        if self.kaugus >= liikumine:
            self.kaugus = 0
            self.samme = 0
            self.asukoht =+ 1
            
        self.x = liigux
        self.y = liiguy
        
