import pygame, sys, actors, time

## variáveis globais ##
FPS = 10

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
BACKGROUND_COLOR = (255,255,255)

DISPLAYSURF = None
PONTUACAO = 0
TAMANHO_COBRA = 1

## MAIN ##
def main():
    global DISPLAYSURF, PONTUACAO, TAMANHO_COBRA

    pygame.init()

    jogador = []
    comida = actors.food()   

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")

    for i in range(TAMANHO_COBRA):
        jogador.append(actors.snake(440,330,"esquerda"))
    
    while True:
        DISPLAYSURF.fill(BACKGROUND_COLOR)

        ## Movimento da cabeça da cobra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:                           
                if event.key == pygame.K_LEFT:                   
                    jogador[0].mover_x = -50
                    jogador[0].mover_y = 0
                    jogador[0].direcao = "esquerda"
                elif event.key == pygame.K_RIGHT:
                    jogador[0].mover_x = 50
                    jogador[0].mover_y = 0    
                    jogador[0].direcao = "direita"
                elif event.key == pygame.K_UP:
                    jogador[0].mover_y = -50
                    jogador[0].mover_x = 0
                    jogador[0].direcao = "cima"
                elif event.key == pygame.K_DOWN:
                    jogador[0].mover_y = 50 
                    jogador[0].mover_x = 0
                    jogador[0].direcao = "baixo"      

        jogador[0].movimento(DISPLAYSURF)           
        comida.desenhar_comida(DISPLAYSURF)
       
        for i in range(TAMANHO_COBRA-1, 0, -1):
            jogador[i].desenha_cobra(DISPLAYSURF)
            if jogador[i-1].direcao == "esquerda":
                jogador[i].x = jogador[i-1].x
                jogador[i].y = jogador[i-1].y
            elif jogador[i-1].direcao == "direita":
                jogador[i].x = jogador[i-1].x
                jogador[i].y = jogador[i-1].y
            elif jogador[i-1].direcao == "cima":
                jogador[i].x = jogador[i-1].x 
                jogador[i].y = jogador[i-1].y
            elif jogador[i-1].direcao == "baixo":
                jogador[i].x = jogador[i-1].x 
                jogador[i].y = jogador[i-1].y           

        ## Criar cauda da cobra
        if jogador[0].teste_colisao(comida):
            PONTUACAO = PONTUACAO + 10
            comida.gerar_comida(DISPLAYSURF)
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

        pygame.display.update()  
        FPSCLOCK.tick(FPS)  

## MAIN ##
if __name__ == '__main__':
    main()
