import pygame
from player import Jugador
from player import Enemigo

pygame.init()
screen = pygame.display.set_mode((1082,720))
mi_Rect = pygame.Rect(1052, 690, 20, 20)
enemigo_Rect = pygame.Rect(20,20,20,20)
velocidad = 5
velocidad_enemigo = 2 
clock = pygame.time.Clock()
running = True
mijugador = Jugador("Juan",mi_Rect,velocidad, 'black')
enemigo1 = Enemigo("malo",enemigo_Rect, velocidad_enemigo, 'blue' )


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
            
    
    mijugador.caminar(keys)
    enemigo1.perseguir(mijugador)
    mijugador.revisar_colision(enemigo1)
    
        
            
    screen.fill('orange')
        
    
    mijugador.dibujar(screen)
    enemigo1.dibujar(screen)
    
    pygame.display.flip()
    
    
    clock.tick(60)
    
    
pygame.quit()