import pygame

pygame.init()
screen = pygame.display.set_mode((1082,720))
jugador = pygame.Rect(1052, 690, 20, 20)
velocidad = 5
clock = pygame.time.Clock()
running = True


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        jugador.x += velocidad
        
    if keys[pygame.K_LEFT]:
        jugador.x -= velocidad
        
    if keys[pygame.K_UP]:
        jugador.y -= velocidad
        
    if keys[pygame.K_DOWN]:
        jugador.y += velocidad
        
    if jugador.x < 0:
        jugador.x = 0 
        
    if jugador.x > 1062:
        jugador.x = 1062
        
    if jugador.y < 0:
        jugador.y = 0
        
    if jugador.y > 700:
        jugador.y = 700
        
            
    screen.fill('orange')
        
    
    pygame.draw.rect(screen,'black', jugador)
    
    pygame.display.flip()
    
    
    clock.tick(60)
    
    
pygame.quit()