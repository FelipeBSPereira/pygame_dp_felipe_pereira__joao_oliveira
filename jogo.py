import pygame as py
import time
from funcoes import *
# py.init()
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



WIDTH = 1400
HEIGHT = 700

py.init()

window= py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption ('Crossy Pica-pau')
clock = py.time.Clock ()

pontos = 0
pontos_font = py.font.SysFont ('comicsans', 44 , True)

fundo = Tela()
screen_group = py.sprite.Group()
screen_group.add(fundo)

picapau =picapau()
grupo_picapau = py.sprite.Group()
grupo_picapau.add(picapau)

zeca_urubu = viloes(1)
leoncio = viloes(2)
grupo_viloes = py.sprite.Group()
grupo_viloes.add(leoncio,zeca_urubu)

torta1= Torta(1)
torta2= Torta(2)
grupo_torta=py.sprite.Group()
grupo_torta.add(torta1,torta2)
tortas= [torta1,torta2]

#somJG= py.mixer.Sound("música_jogo")
#somD= py.mixer.Sound("perdeu")
#somR= py.mixer.Sound("risada")


#captura= captura()
jogo=True
game = True

while game :
    
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False

    screen_group.draw(window)

    grupo_viloes.draw(window)
    grupo_picapau.draw(window)
    grupo_torta.draw(window)


    grupo_viloes.update()
    grupo_picapau.update()
    grupo_torta.update()
    screen_group.update()
    

    py.display.update()
py.quit()


