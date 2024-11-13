
class Tela(py.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.t_jogo = py.image.load ('tela_jogo.png')
        self.t_final = py.image.load ('tela_final.png')

        self.t_jogo = py.transform.scale (self.t_jogo,(WIDTH,HEIGHT))
        self.t_final = py.transform.scale (self.t_final,(WIDTH,HEIGHT))

        self.image = self.t_jogo
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()

        def arruma (self):
            self.rect.topleft = (self.x,self.y)