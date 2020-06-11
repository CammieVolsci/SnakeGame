import pygame, random, datetime

SNAKE_IMAGE = "assets/snake.png"
FOOD_IMAGE = "assets/food.png"

class snake(pygame.sprite.Sprite):
    
    def __init__(self,x,y,direcao):
        super().__init__()
        self.x = x
        self.y = y
        self.mover_x = 0
        self.mover_y = 0
        self.direcao = direcao
        self.image = pygame.image.load(SNAKE_IMAGE)    
        self.rect = self.image.get_rect()
        self.dead = False

    def desenhar(self,screen):       
        screen.blit(self.image,(self.x,self.y))   

    def movimento_cabeca(self):       
        self.x += self.mover_x
        self.y += self.mover_y

        self.rect.x = self.x
        self.rect.y = self.y 

        if self.x <= 5:
            self.x = 5
            self.mover_x = 0
            self.dead = True
        elif self.x + 50 >= 795:
            self.x = 745
            self.mover_x = 0
            self.dead = True

        if self.y <= 5:
            self.y = 5
            self.mover_y = 0
            self.dead = True
        elif self.y + 50 >= 645:
            self.y = 595
            self.mover_y = 0
            self.dead = True

        self.rect.x = self.x
        self.rect.y = self.y     

    def teste_colisao(self,sprite):
        if(self.image!=0):
            return self.rect.colliderect(sprite.rect)   

class food(pygame.sprite.Sprite):

    random.seed(datetime.time())  

    def __init__(self):
        super().__init__()
        self.x = random.randint(50,750) 
        self.y = random.randint(50,600)
        self.image = pygame.image.load(FOOD_IMAGE)
        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y   
        self.boa_localizacao = False
    
    def desenhar(self,screen):
        screen.blit(self.image,(self.x,self.y))         

    def gerar(self):               
        self.x = random.randint(50,750) 
        self.y = random.randint(50,600) 
        self.rect.x = self.x
        self.rect.y = self.y 

    def teste_colisao(self,sprite):
        if(self.image!=0):
            return self.rect.colliderect(sprite.rect)   
