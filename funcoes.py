import pygame as py
from parametros2 import *

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
        return len(colisao_viloes) > 0       

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
        self.t_jogo = py.image.load ('assets/fundo_teste.png')
        self.t_final = py.image.load ('assets/fundo_teste.png')

        self.t_jogo = py.transform.scale (self.t_jogo,(WIDTH,HEIGHT))
        self.t_final = py.transform.scale (self.t_final,(WIDTH,HEIGHT))

        self.image = self.t_jogo
        print(self.image)
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()

        def arruma (self):
            self.rect.topleft = (self.x,self.y)

def sobenivel():
    global nivel, pontos
    nivel += 1
    for viloes in  grupo_viloes:
        if viloes.vel < 0:
            viloes.vel -= 1
        else:
            viloes.vel += 1
def tela_fim():
    global pontos, recorde, jogo
    texto_final= pontos_font.render("Pontuação: " + str(pontos), True, (255, 0, 0))
    texto_recorde = pontos_font.render("Recorde: " + str(recorde), True, (0, 255, 0))
    texto_reiniciar = pontos_font.render("Pressione R para reiniciar", True, (255, 255, 255))
    window.fill((0, 0, 0))
    window.blit(texto_final, (WIDTH / 2 - texto_final.get_width() / 2, HEIGHT / 2 - 50))
    window.blit(texto_recorde, (WIDTH / 2 - texto_recorde.get_width() / 2, HEIGHT / 2))
    window.blit(texto_reiniciar, (WIDTH / 2 - texto_reiniciar.get_width() / 2, HEIGHT / 2 + 50))
    py.display.flip()
    while not jogo:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type == py.KEYDOWN and event.key == py.K_r:
                reinicia_jogo()
def reinicia_jogo():
    global pontos, nivel, jogo
    pontos = 0
    nivel = 1
    jogo = True
    picapau.x = 50
    picapau.y = HEIGHT / 2
    for viloes in grupo_viloes:
        viloes.y = HEIGHT / 2
        viloes.vel = 4  

# def main():
#     global pontos, jogo
#     pontos_alvo = 5 
#     while True:
#         clock.tick(60)
#         for event in py.event.get():
#             if event.type == py.QUIT:
#                 py.quit()
#                 exit()

#         if jogo:
#             window.fill((255, 255, 255)) 
#             grupo_picapau.update()
#             grupo_viloes.update()
#             grupo_picapau.draw(window)
#             grupo_viloes.draw(window)
#             pontos_texto = pontos_font.render("Pontuação: " + str(pontos), True, (0, 0, 0))
#             nivel_texto = pontos_font.render("Nível: " + str(nivel), True, (0, 0, 0))
#             window.blit(pontos_texto, (10, 10))
#             window.blit(nivel_texto, (10, 60))
#             py.display.update()
#             pontos += 1
#             if pontos >= pontos_alvo * nivel:
#                 sobenivel()
#         else:
#             tela_fim()

picapau1 = picapau()
grupo_picapau = py.sprite.Group(picapau1)
zeca_urubu = viloes(1)
leoncio = viloes(2)
grupo_viloes = py.sprite.Group(zeca_urubu, leoncio)


# py.init()

# window= py.display.set_mode((WIDTH,HEIGHT))
# py.display.set_caption ('Crossy Pica-pau')
# clock = py.time.Clock ()

# pontos = 0
# pontos_font = py.font.SysFont ('comicsans', 44 , True)

# fundo = Tela ()
# screen_group = py.sprite.Group()
# screen_group.add(fundo)

# picapau =picapau()
# grupo_picapau = py.sprite.Group()
# grupo_picapau.add(picapau)

# zeca_urubu = viloes(1)
# leoncio = viloes(2)
# grupo_picapau = py.sprite.Group()
# grupo_viloes.add(leoncio,zeca_urubu)

# torta1= Torta(1)
# torta2= Torta(2)
# grupo_torta=py.sprite.Group()
# grupo_torta.add(torta1,torta2)
# tortas= [torta1,torta2]

# #somJG= py.mixer.Sound("música_jogo")
# #somD= py.mixer.Sound("perdeu")
# #somR= py.mixer.Sound("risada")


# #captura= capture() 
# jogo=True
# game = True

# while game :
    
#     clock.tick(60)
#     for event in py.event.get():
#         if event.type == py.QUIT:
#             game = False

#     screen_group.draw(window)

#     grupo_viloes.draw(window)
#     grupo_picapau.draw(window)
#     grupo_torta.draw(window)
#     grupo_viloes.update()
#     grupo_picapau.update()
#     grupo_torta.update()
#     screen_group.update()
    

#     py.display.update()
# py.quit()