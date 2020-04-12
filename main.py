import pygame, sys, actors

## variáveis globais ##
FPS = 30

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
BACKGROUND_COLOR = (255,255,255)

DISPLAYSURF = None
PONTUACAO = None

## MAIN ##
def main():
    global DISPLAYSURF, PONTUACAO

    pygame.init()

    jogador = actors.snake()
    comida = actors.food()   
    game_status = "COMECAR"

    PONTUACAO = 0
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    
    while True:
        DISPLAYSURF.fill(BACKGROUND_COLOR)

        ## Movimento do jogador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    jogador.mover_x = -5
                    jogador.mover_y = 0
                elif event.key == pygame.K_RIGHT:
                    jogador.mover_x = 5 
                    jogador.mover_y = 0    
                elif event.key == pygame.K_UP:
                    jogador.mover_y = -5
                    jogador.mover_x = 0
                elif event.key == pygame.K_DOWN:
                    jogador.mover_y = 5      
                    jogador.mover_x = 0

        jogador.movimento(DISPLAYSURF)      
        comida.desenhar_comida(DISPLAYSURF)

        if jogador.teste_colisao(comida):
            print("colidiu")
            PONTUACAO = PONTUACAO + 10
            comida.gerar_comida(DISPLAYSURF)

        pygame.display.update()  
        FPSCLOCK.tick(FPS)  

## MAIN ##
if __name__ == '__main__':
    main()
