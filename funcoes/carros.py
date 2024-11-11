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