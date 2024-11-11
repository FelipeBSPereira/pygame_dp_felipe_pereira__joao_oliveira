class carros(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT/2
        self.vel = 4
        self.widht = 100
        self.height = 50

        self.carro1 = py.image.load ('carro_para_direita.png')
        self.carro2 = py.image.load ('carro_para_esquerda.png')
        self.carro1 = py.transform.scale(self.carro1,(self.widht,self.height))
        self.carro2 = py.transform.scale(self.carro2,(self.widht,self.height))
        self.image = self.carro1
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
            self.image = self.capy2
        elif keys [py.K_RIGHT]:
            self.x += self.vel
            self.image = self.capy1
        if keys [py.K_UP]:
            self.y -= self.vel
        elif keys [py.K_DOWN]:
            self.y += self.vel