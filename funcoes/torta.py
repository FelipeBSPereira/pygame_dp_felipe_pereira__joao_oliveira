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


