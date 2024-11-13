WIDTH = 1400
HEIGHT = 800

py.init()

window= py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption ('Crossy Pica-pau')
clock = py.time.Clock ()

pontos = 0
pontos_font = py.font.SysFont ('comicsans', 44 , True)

fundo = Tela ()
screen_group = py.sprite.Group()
screen_group.add(fundo)

picapau =picapau()
picapau_group = py.sprite.Group()
picapau_group.add(picapau)

carro_1 = carro(1)
carro_2 = carro(2)
group_carro = py.sprite.Group()
group_carro.add(carro_1,carro_2)

torta1= torta(1)
torta2= torta(2)
group_torta=py.sprite.Group()
group_torta.add(torta1,torta2)
tortas= [torta1,torta2]

somJG= py.mixer.Sound("música_jogo")
somD= py.mixer.Sound("perdeu")
somR= py.mixer.Sound("risada")


captura= captura()
jogo=True
game = True

while game :

    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False

    screen_group.draw(window)

    pontodpl()
    checatorta()

    group_carro.draw(window)
    picapau_group.draw(window)
    group_torta.draw(window)
    group_carro.update()
    picapau_group.update()
    group_torta.update()
    screen_group.update()
    

    py.display.update()
py.quit()