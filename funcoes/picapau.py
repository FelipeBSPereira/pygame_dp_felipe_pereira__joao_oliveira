class picapau(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT/2
        self.vel = 4
        self.widht = 100
        self.height = 50

        self.picapau1 = py.image.load('picapau_para_direita.png')
        self.picapau2 = py.image.load('picapau_para_esquerda.png')
        self.picapau1 = py.transform.scale(self.picapau1,(self.widht,self.height))
        self.picapau2 = py.transform.scale(self.picapau2,(self.widht,self.height))
        self.image = self.picapau1
        self.rect = self.image.get_rect()
        self.mask= py.mask.from_surface(self.image)

    def update (self):
        self.movement()
        self.correction()
        self.Checaimpacto()
        self.rect.center = (self.x,self.y)
    
    def movement (self):
        keys = py.key.get_pressed()
        if keys [py.K_LEFT]:
            self.x -= self.vel
            self.image = self.picapau2
        elif keys [py.K_RIGHT]:
            self.x += self.vel
            self.image = self.picapau1
        if keys [py.K_UP]:
            self.y -= self.vel
        elif keys [py.K_DOWN]:
            self.y += self.vel
    def correction (self):
        if self.x - self.widht / 2 < 0 :
            self.x = self.widht / 2

        elif self.x + self.widht / 2 > WIDTH:
            self.x = WIDTH - self.widht / 2

        if self.y - self.height / 2 < 0 :
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
    def Checaimpacto(self):
        mbpC=py.sprite.spritecollide(self, group_mbp, False, py.sprite.collide_mask)
        if mbpC:
            somExp.play()
            explosao.explode(self.x, self.y)