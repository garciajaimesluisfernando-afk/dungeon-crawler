import pygame

class Jugador:
    def __init__(self, nombre, rect, velocidad, color):
        self.nombre = nombre
        self.rect = rect
        self.velocidad = velocidad
        self.color = color
        
        
    def caminar(self, keys):
        
        if keys[pygame.K_RIGHT]:
                self.rect.x += self.velocidad
                
        if keys[pygame.K_LEFT]:
                self.rect.x -= self.velocidad
                
        if keys[pygame.K_UP]:
                self.rect.y -= self.velocidad
                
        if keys[pygame.K_DOWN]:
                self.rect.y += self.velocidad
                
        if self.rect.x < 0:
                self.rect.x = 0 
                
        if self.rect.x > 1062:
            self.rect.x = 1062
                
        if self.rect.y < 0:
            self.rect.y = 0
                
        if self.rect.y > 700:
            self.rect.y = 700
            
    def dibujar(self, screen):
        pygame.draw.rect(screen,'black', self.rect)
        
class Enemigo(Jugador):
        def __init__(self, nombre, rect, velocidad, color):
                super().__init__(nombre, rect, velocidad, color)
                
                
        def perseguir(self, jugador):
                
                if jugador.rect.x > self.rect.x:
                        self.rect.x += self.velocidad
                        
                if jugador.rect.x < self.rect.x:
                        self.rect.x -= self.velocidad
                        
                if jugador.rect.y >  self.rect.y:
                        self.rect.y += self.velocidad
                        
                if jugador.rect.y < self.rect.y:
                        self.rect.y -= self.velocidad