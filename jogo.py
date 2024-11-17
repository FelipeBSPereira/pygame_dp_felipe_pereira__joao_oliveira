import pygame as py
from parametros2 import *
from funcoes import *

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
