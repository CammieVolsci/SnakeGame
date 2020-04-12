import pygame, random, datetime

SNAKE_IMAGE = "assets/snake.png"
FOOD_IMAGE = "assets/food.png"

class snake(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.x = 440
        self.y = 330
        self.mover_x = 0
        self.mover_y = 0
        self.direcao = "direita"
        self.image = pygame.image.load(SNAKE_IMAGE)    
        self.rect = self.image.get_rect() 

    def movimento(self,screen):       
        self.x += self.mover_x
        self.y += self.mover_y
        screen.blit(self.image,(self.x,self.y))

        self.rect.x = self.x
        self.rect.y = self.y 

        if self.x <= 0:
            self.x = 750
        elif self.x >= 750:
            self.x = 0

        if self.y <= 0:
            self.y = 600
        elif self.y >= 600:
            self.y = 0

        self.rect.x = self.x
        self.rect.y = self.y      

    def teste_colisao(self,sprite):
        if(self.image!=0):
            return self.rect.colliderect(sprite.rect)   

class food(pygame.sprite.Sprite):

    random.seed(datetime.time())  

    def __init__(self):
        super().__init__()
        self.x = random.randint(25,775) 
        self.y = random.randint(25,625)
        self.image = pygame.image.load(FOOD_IMAGE)
        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y    
    
    def desenhar_comida(self, screen):
        screen.blit(self.image,(self.x,self.y))         

    def gerar_comida(self,screen):               
        self.x = random.randint(25,775) 
        self.y = random.randint(25,625) 
        self.rect.x = self.x
        self.rect.y = self.y 