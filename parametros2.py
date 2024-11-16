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
recorde = 0
jogo = True


py.mixer.init()
#som_jogo = py.mixer.Sound('musica_fundo.mp3')
som_torta = py.mixer.Sound('som_torta.mp3')
som_perda = py.mixer.Sound('som_perda.mp3')

#py.mixer.Sound.play(som_jogo, loops=-1)

screen_group = py.sprite.Group()
grupo_picapau = py.sprite.Group()
grupo_viloes = py.sprite.Group()
grupo_torta = py.sprite.Group()
