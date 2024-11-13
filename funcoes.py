class picapau(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT/2
        self.vel = 4
        self.widht = 100
        self.height = 50

        self.picapau1 = py.image.load('picapau_direita.png')
        self.picapau2 = py.image.load('picapau_esquerda.png')
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
        picapauC=py.sprite.spritecollide(self, group_mbp, False, py.sprite.collide_mask)

class viloes(py.sprite.Sprite):
    def __init__ (self,numero):
        super().__init__()
        if numero == 1:
            self.x = 380
            self.image = py.image.load ('carro.png')
            self.vel = -4
        else:
            self.x = 920
            self.image = py.image.load ('carro.png')
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

class Torta(py.sprite.Sprite):
    def __init__(self, quantidade):
        super().__init__()
        self.quantidade = quantidade
        self.imagem = py.image.load('imagem_torta.png')
        self.visivel = quantidade != 1
        self.posicao_x = 1200 if quantidade != 1 else 200
        self.posicao_y = HEIGHT / 2
        
        self.imagem = py.transform.scale2x(self.imagem)
        self.retangulo = self.imagem.get_rect()
        self.mascara = py.mask.from_surface(self.imagem)
    
    def atualizar(self, grupo_personagens, pontos):
        if self.visivel:
            self.verificar_colisao(grupo_personagens, pontos)
            self.retangulo.center = (self.posicao_x, self.posicao_y)

    def verificar_colisao(self, grupo_personagens, pontos):
        colisao_detectada = py.sprite.spritecollide(self, grupo_personagens, False, py.sprite.collide_mask)
        if colisao_detectada:
            self.visivel = False
            somB.play()
            
            if self.quantidade == 1:
                torta_b.visivel = True
                if pontos < 5:
                    aumentar_nivel()
                else:
                    grupo_personagens.empty()
                    resetar_jogo()
                    exibir_tela_final(1)
            else:
                torta_a.visivel = True

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
