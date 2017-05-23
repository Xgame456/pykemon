
import pygame
from pygame.locals import * 

centre_x = -1
centre_y = -1
def rot_center(image, rect, angle):
        #rotate une image va le garder au centre
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def spawn():
        x = randint(0,9)
        y = randint(0,9)
        #while(maps.map_1[y][x] ==== 5):
               # x = randint(0,9)
               # y = randint(0,9)
        #retunr x * 800 + centre_x, y*600 + centre_y
        
class Perso:
        def __init__(self, droite, gauche, haut, bas):
                self.droite = pygame.image.load(droite).convert_alpha()
                self.gauche = pygame.image.load(gauche).convert_alpha()
                self.haut = pygame.image.load(haut).convert_alpha()
                self.bas = pygame.image.load(bas).convert_alpha()
                #self.fenetre = pygame.dislay.get_surface()
                #self.fond = self.fenetre.get_rect()
                
		#Position du personnage en cases et en pixels
                self.case_x = 0
                self.case_y = 0
                self.x = 200
                self.y = 250
		#Direction par défaut
                self.direction = self.bas
        def deplacer(self, direction):
                if direction == 'bas': 
                        self.direction = self.bas
                        self.y += 3           
                if direction == 'haut':
                        self.direction = self.haut
                        self.y -= 3
                if direction == 'gauche':    
                        self.direction = self.gauche
                        self.x -= 3		
                if direction == 'droite':
                        self.direction = self.droite
                        self.x += 3
		

	


      		
		
		
			
			
		
		
		
			

         	
