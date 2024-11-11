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
    
    def update (self):
        self.movement()
        self.rect.center = (self.x, self.y)


    def movement (self):
        self.y += self.vel
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1
        
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1