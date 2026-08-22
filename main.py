import pygame
from player import Jugador

pygame.init()
screen = pygame.display.set_mode((1082,720))
mi_Rect = pygame.Rect(1052, 690, 20, 20)
velocidad = 5
clock = pygame.time.Clock()
running = True
mijugador = Jugador("Juan",mi_Rect,velocidad, 'black')


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
            
    
    mijugador.caminar(keys)
    
        
            
    screen.fill('orange')
        
    
    mijugador.dibujar(screen)
    
    pygame.display.flip()
    
    
    clock.tick(60)
    
    
pygame.quit()