import pygame, actors
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)

class SnakeGame:
    
    window_width = None
    window_height = None   
    background = None
    displaysurf = None 
    run = True
    fps = None
    reset = False

    basic_font = None
    tamanho_cobra = 1
    pontuacao = 0  

    jogador = []
    comida = None     

    def __init__(self):
        self.window_width = 800
        self.window_height = 650
        self.fps = 30   
        pygame.init()
        pygame.display.set_caption("SnakeGame")
        self.displaysurf = pygame.display.set_mode((self.window_width,self.window_height))   
        self.basic_font = pygame.font.Font('freesansbold.ttf',32)     
    
    def handle_events(self):
        for event in pygame.event.get():
            t = event.type
            if t in (KEYDOWN,KEYUP):
                k = event.key
            if t == QUIT:
                self.run = False
            elif t == KEYDOWN:
                if k == K_ESCAPE:
                    self.run = False
                if k == K_r:
                    self.reset = True
                if k == K_LEFT and not self.jogador[0].dead:
                    if self.tamanho_cobra == 1 or (self.tamanho_cobra > 1 and self.jogador[1].direcao != "direita"):    
                        self.jogador[0].mover_x = -50
                        self.jogador[0].mover_y = 0
                        self.jogador[0].direcao = "esquerda"
                elif k == K_RIGHT and not self.jogador[0].dead:
                    if self.tamanho_cobra == 1 or (self.tamanho_cobra > 1 and self.jogador[1].direcao != "esquerda"):
                        self.jogador[0].mover_x = 50
                        self.jogador[0].mover_y = 0    
                        self.jogador[0].direcao = "direita"
                elif k == K_UP and not self.jogador[0].dead:
                    if self.tamanho_cobra == 1 or (self.tamanho_cobra > 1 and self.jogador[1].direcao != "baixo"):
                        self.jogador[0].mover_y = -50
                        self.jogador[0].mover_x = 0
                        self.jogador[0].direcao = "cima"
                elif k == K_DOWN and not self.jogador[0].dead:
                    if self.tamanho_cobra == 1 or (self.tamanho_cobra > 1 and self.jogador[1].direcao != "cima"):
                        self.jogador[0].mover_y = 50
                        self.jogador[0].mover_x = 0
                        self.jogador[0].direcao = "baixo"                   

    def actors_update(self):

        self.jogador[0].movimento_cabeca()  

        if self.tamanho_cobra > 1:
            for i in range(1,self.tamanho_cobra):
                if self.jogador[0].teste_colisao(self.jogador[i]):
                    self.jogador[0].mover_x = 0
                    self.jogador[0].mover_y = 0
                    self.jogador[0].dead = True 

        if self.jogador[0].teste_colisao(self.comida):      
            self.pontuacao += 10
            self.comida.boa_localizacao = False  
            if self.jogador[self.tamanho_cobra-1].direcao == "esquerda":
                self.jogador.append(actors.snake(self.jogador[self.tamanho_cobra-1].x+50,self.jogador[self.tamanho_cobra-1].y,"esquerda"))
                self.tamanho_cobra += 1
            elif self.jogador[self.tamanho_cobra-1].direcao == "direita":
                self.jogador.append(actors.snake(self.jogador[self.tamanho_cobra-1].x-50,self.jogador[self.tamanho_cobra-1].y,"direita"))
                self.tamanho_cobra += 1
            elif self.jogador[self.tamanho_cobra-1].direcao == "cima":
                self.jogador.append(actors.snake(self.jogador[self.tamanho_cobra-1].x,self.jogador[self.tamanho_cobra-1].y+50,"cima"))
                self.tamanho_cobra += 1
            elif self.jogador[self.tamanho_cobra-1].direcao == "baixo":
                self.jogador.append(actors.snake(self.jogador[self.tamanho_cobra-1].x,self.jogador[self.tamanho_cobra-1].y-50,"baixo"))
                self.tamanho_cobra += 1

            self.jogador[self.tamanho_cobra-1].rect.x =  self.jogador[self.tamanho_cobra-1].x  
            self.jogador[self.tamanho_cobra-1].rect.y =  self.jogador[self.tamanho_cobra-1].y     

            while(not self.comida.boa_localizacao):
                self.comida.boa_localizacao = True
                self.comida.gerar()
                for i in range(self.tamanho_cobra):    
                    if self.jogador[i].teste_colisao(self.comida):      
                        self.comida.boa_localizacao = False

        for i in range(self.tamanho_cobra-1,0,-1):
            self.jogador[i].direcao = self.jogador[i-1].direcao
            self.jogador[i].x = self.jogador[i-1].x
            self.jogador[i].y = self.jogador[i-1].y
            self.jogador[i].rect.x =  self.jogador[i].x  
            self.jogador[i].rect.y =  self.jogador[i].y       



    def actors_draw(self):

        for i in range(self.tamanho_cobra):
            self.jogador[i].desenhar(self.displaysurf)

        self.comida.desenhar(self.displaysurf)


    def loop(self):
        fpsclock = pygame.time.Clock()   
        self.comida = actors.food()
        self.fps = 5

        for i in range(self.tamanho_cobra):
            self.jogador.append(actors.snake(400,350,"esquerda"))

        while self.run:    
            self.displaysurf.fill(WHITE) 

            if self.reset == True:
                self.self.jogador.clear()
                self.tamanho_cobra = 1
                self.pontuacao = 0
                for i in range(self.tamanho_cobra):
                    self.self.jogador.append(actors.snake(400,350,"esquerda"))   
                self.reset = False

            self.handle_events()
            self.actors_draw()   
            self.actors_update()     
          
            
            pygame.display.flip()
            pygame.display.update()  
            fpsclock.tick(self.fps)

def main():
    game = SnakeGame()
    game.loop()

## MAIN ##
if __name__ == '__main__':
    main()
