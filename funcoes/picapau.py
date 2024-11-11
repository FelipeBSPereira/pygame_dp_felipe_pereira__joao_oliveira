class picapau(py.sprite.Sprite):
    def __init__ (self,numero):
        super().__init__()
        if numero == 1:
            self.x = 380
            self.image = py.image.load ('picapau.png')
            self.vel = -4
        else:
            self.x = 920
            self.image = py.image.load ('picapau.png')
            self.vel = 5
        
        self.y = HEIGHT / 2
        self.widht = 100
        self.height = 150
        self.image = py.transform.scale(self.image,(self.widht,self.height))
        self.rect = self.image.get_rect()
        self.mask= py.mask.from_surface(self.image)