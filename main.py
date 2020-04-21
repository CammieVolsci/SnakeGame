import pygame, sys, actors, time

## variáveis globais ##
FPS = 5

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
BACKGROUND_COLOR = (255,255,255)

DISPLAYSURF = None
PONTUACAO = 1
TAMANHO_COBRA = 1

## MAIN ##
def main():
    global DISPLAYSURF, PONTUACAO, TAMANHO_COBRA

    pygame.init()

    jogador = []
    comida = actors.food()   
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)
    pygame.display.set_caption("Snake")

    for i in range(TAMANHO_COBRA):
        jogador.append(actors.snake(400,350,"esquerda"))
    
    while True:
        DISPLAYSURF.fill(BACKGROUND_COLOR)
        gameOverSurf = BASICFONT.render('Game Over',True,(0,0,0))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (400, 325)  

        if jogador[0].dead:
            DISPLAYSURF.blit(gameOverSurf,gameOverRect)
            main()

        movimenta_cabeca_cobra(jogador)
        jogador[0].movimento_cabeca(DISPLAYSURF)

        if TAMANHO_COBRA > 1:
            for i in range(1,TAMANHO_COBRA):
                if jogador[0].teste_colisao(jogador[i]):
                    jogador[0].mover_x = 0
                    jogador[0].mover_y = 0
                    jogador[0].dead = True

        comida.desenhar_comida(DISPLAYSURF)       
        cria_cauda_cobra(jogador,comida)
        movimenta_cauda_cobra(jogador)           

        pygame.display.update()  
        FPSCLOCK.tick(FPS)  

def movimenta_cabeca_cobra(jogador):
    global TAMANHO_COBRA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and not jogador[0].dead:                           
            if event.key == pygame.K_LEFT:
                if TAMANHO_COBRA == 1 or (TAMANHO_COBRA > 1 and jogador[1].direcao != "direita"):    
                    jogador[0].mover_x = -50
                    jogador[0].mover_y = 0
                    jogador[0].direcao = "esquerda"
            elif event.key == pygame.K_RIGHT:
                if TAMANHO_COBRA == 1 or (TAMANHO_COBRA > 1 and jogador[1].direcao != "esquerda"):
                    jogador[0].mover_x = 50
                    jogador[0].mover_y = 0    
                    jogador[0].direcao = "direita"
            elif event.key == pygame.K_UP:
                if TAMANHO_COBRA == 1 or (TAMANHO_COBRA > 1 and jogador[1].direcao != "baixo"):
                    jogador[0].mover_y = -50
                    jogador[0].mover_x = 0
                    jogador[0].direcao = "cima"
            elif event.key == pygame.K_DOWN:
                if TAMANHO_COBRA == 1 or (TAMANHO_COBRA > 1 and jogador[1].direcao != "cima"):
                    jogador[0].mover_y = 50 
                    jogador[0].mover_x = 0
                    jogador[0].direcao = "baixo"    

def movimenta_cauda_cobra(jogador):

    for i in range(TAMANHO_COBRA-1, 0, -1):
        jogador[i].desenha_cobra(DISPLAYSURF)
        jogador[i].direcao = jogador[i-1].direcao
        jogador[i].x = jogador[i-1].x
        jogador[i].y = jogador[i-1].y

        jogador[i].rect.x =  jogador[i].x  
        jogador[i].rect.y =  jogador[i].y   

def cria_cauda_cobra(jogador,comida):

    global PONTUACAO, TAMANHO_COBRA

    if jogador[0].teste_colisao(comida):
        
        PONTUACAO = PONTUACAO + 10     
        comida.boa_localizacao = False   

        if jogador[TAMANHO_COBRA-1].direcao == "esquerda":
            jogador.append(actors.snake(jogador[TAMANHO_COBRA-1].x+50,jogador[TAMANHO_COBRA-1].y,"esquerda"))
            TAMANHO_COBRA += 1
        elif jogador[TAMANHO_COBRA-1].direcao == "direita":
            jogador.append(actors.snake(jogador[TAMANHO_COBRA-1].x-50,jogador[TAMANHO_COBRA-1].y,"direita"))
            TAMANHO_COBRA += 1
        elif jogador[TAMANHO_COBRA-1].direcao == "cima":
            jogador.append(actors.snake(jogador[TAMANHO_COBRA-1].x,jogador[TAMANHO_COBRA-1].y+50,"cima"))
            TAMANHO_COBRA += 1
        elif jogador[TAMANHO_COBRA-1].direcao == "baixo":
            jogador.append(actors.snake(jogador[TAMANHO_COBRA-1].x,jogador[TAMANHO_COBRA-1].y-50,"baixo"))
            TAMANHO_COBRA += 1

        jogador[TAMANHO_COBRA-1].rect.x =  jogador[TAMANHO_COBRA-1].x  
        jogador[TAMANHO_COBRA-1].rect.y =  jogador[TAMANHO_COBRA-1].y     

        while(not comida.boa_localizacao):
            comida.boa_localizacao = True
            comida.gerar_comida(DISPLAYSURF)
            for i in range(TAMANHO_COBRA):    
                if jogador[i].teste_colisao(comida):      
                    comida.boa_localizacao = False                             

## MAIN ##
if __name__ == '__main__':
    main()

