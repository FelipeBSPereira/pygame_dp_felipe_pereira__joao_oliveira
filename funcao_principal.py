# O jogo estava funcionando com erros separado, quando juntamos para identificar os erros ele passou a funcionar


import pygame as py


WIDTH = 1400
HEIGHT = 700


py.init()


window = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('Crossy Pica-pau')
clock = py.time.Clock()


pontos_font = py.font.SysFont('comicsans', 44, True)
final_font = py.font.SysFont('comicsans', 64, True)


pontos = 0
nivel = 1
recorde = 0
jogo = True

py.mixer.init()
#som_jogo = py.mixer.Sound('musica_fundo.mp3')
som_torta = py.mixer.Sound('assets/som_torta.mp3')
som_perda = py.mixer.Sound('assets/som_perda.mp3')

#py.mixer.Sound.play(som_jogo, loops=-1)


screen_group = py.sprite.Group()
grupo_picapau = py.sprite.Group()
grupo_viloes = py.sprite.Group()
grupo_torta = py.sprite.Group()


class picapau(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT / 2
        self.vel = 4
        self.width = 100
        self.height = 50

        self.picapau1 = py.image.load('assets/picapau_direita.png').convert_alpha()
        self.picapau2 = py.image.load('assets/picapau_esquerda.png').convert_alpha()
        self.picapau1 = py.transform.scale(self.picapau1, (self.width, self.height))
        self.picapau2 = py.transform.scale(self.picapau2, (self.width, self.height))
        self.image = self.picapau1
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.mask = py.mask.from_surface(self.image)

    def reset(self):
        self.x = 50
        self.y = HEIGHT / 2
        self.image = self.picapau1
        self.rect.center = (self.x, self.y)

    def update(self):
        self.movement()
        self.correction()
        if self.checa_impacto():
            global jogo
            py.mixer.Sound.play(som_perda)
            jogo = False
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            self.x -= self.vel
            self.image = self.picapau2
        elif keys[py.K_RIGHT]:
            self.x += self.vel
            self.image = self.picapau1
        if keys[py.K_UP]:
            self.y -= self.vel
        elif keys[py.K_DOWN]:
            self.y += self.vel

    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2
        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

    def checa_impacto(self):
        colisao_viloes = py.sprite.spritecollide(self, grupo_viloes, False, py.sprite.collide_mask)
        return bool(colisao_viloes)


class viloes(py.sprite.Sprite):
    def __init__(self, numero):
        super().__init__()
        if numero == 1:
            self.x = 380
            self.image = py.image.load('assets/zecaurubu.png').convert_alpha()
            self.vel = -4
        else:
            self.x = 920
            self.image = py.image.load('assets/leoncio.png').convert_alpha()
            self.vel = 5

        self.y = HEIGHT / 2
        self.width = 100
        self.height = 150
        self.image = py.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.mask = py.mask.from_surface(self.image)

    def reset(self):
        self.y = HEIGHT / 2
        self.vel = 4 if self.vel > 0 else -4

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        self.y += self.vel
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1
    def aumenta_velocidade_viloes(self):
        global pontos
        if pontos >= 5:
            nova_velocidade = 5
            if self.vel > 0:
                self.vel = nova_velocidade
            else:
                self.vel = -nova_velocidade


class Torta(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 1170  
        self.y = HEIGHT / 2
        self.image = py.image.load('assets/torta.png').convert_alpha()
        self.image = py.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.mask = py.mask.from_surface(self.image)
        self.lado = 2  

    def reset(self):
        self.lado = 2  
        self.x = 1170
        self.rect.center = (self.x, self.y)

    def update(self):
        self.pega_torta()
        self.rect.center = (self.x, self.y)

    def pega_torta(self):
        global pontos
        pega_torta = py.sprite.spritecollide(self, grupo_picapau, False, py.sprite.collide_mask)
        if pega_torta:
            pontos += 1
            py.mixer.Sound.play(som_torta)
            self.mudar_lado()

    def mudar_lado(self):
        if self.lado == 1:
            self.lado = 2
            self.x = 1170
        else:
            self.lado = 1
            self.x = 130


class Tela(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.t_jogo = py.image.load('assets/mapa1.png').convert_alpha()
        self.t_jogo = py.transform.scale(self.t_jogo, (WIDTH, HEIGHT))
        self.image = self.t_jogo
        self.rect = self.image.get_rect()


def reinicia_jogo():
    global pontos, jogo
    pontos = 0
    jogo = True
    picapau1.reset()
    torta1.reset()
    for vilao in grupo_viloes:
        vilao.reset()


def tela_inicial():
    window.fill((0, 0, 0))  
    titulo = final_font.render("Bem-vindo ao Crossy Pica-pau!", True, (255, 255, 0))
    iniciar_texto = pontos_font.render("Pressione qualquer tecla para começar", True, (255, 255, 255))
    window.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, HEIGHT // 3))
    window.blit(iniciar_texto, (WIDTH // 2 - iniciar_texto.get_width() // 2, HEIGHT // 2))
    py.display.update()

    esperando = True
    while esperando:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type == py.KEYDOWN:
                esperando = False


def tela_final():
    window.fill((0, 0, 0))  
    final_texto = final_font.render("Game Over!", True, (255, 0, 0))
    reinicia_texto = pontos_font.render("Pressione qualquer tecla para reiniciar", True, (255, 255, 255))
    window.blit(final_texto, (WIDTH // 2 - final_texto.get_width() // 2, HEIGHT // 3))
    window.blit(reinicia_texto, (WIDTH // 2 - reinicia_texto.get_width() // 2, HEIGHT // 2))
    py.display.update()

    esperando = True
    while esperando:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type == py.KEYDOWN:
                esperando = False



fundo = Tela()
screen_group.add(fundo)

picapau1 = picapau()
grupo_picapau.add(picapau1)

vilao1 = viloes(1)
vilao2 = viloes(2)
grupo_viloes.add(vilao1, vilao2)

torta1 = Torta()
grupo_torta.add(torta1)


tela_inicial()


running = True
while running:
    clock.tick(60)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    if jogo:
        window.fill((0, 0, 0))  
        screen_group.draw(window)
        grupo_viloes.draw(window)
        grupo_picapau.draw(window)
        grupo_torta.draw(window)
        grupo_viloes.update()
        grupo_picapau.update()
        grupo_torta.update()
        screen_group.update()


        pontos_texto = pontos_font.render(f"Pontuação: {pontos}", True, (255, 255, 255))
        window.blit(pontos_texto, (10, 10))
    else:
        tela_final()
        reinicia_jogo()

    py.display.update()

py.quit()
