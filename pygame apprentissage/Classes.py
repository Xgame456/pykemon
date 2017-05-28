
import pygame
from pygame.locals import *
           
class Perso:
        "Création du personnage"
        def __init__(self, droite, gauche, haut, bas):
                #sprites du personnages
                self.droite = pygame.image.load(droite).convert_alpha()
                self.gauche = pygame.image.load(gauche).convert_alpha()
                self.haut = pygame.image.load(haut).convert_alpha()
                self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
                self.x = 0
                self.y = 0
		#Direction par défaut
                self.direction = self.bas
        def deplacer(self, direction):
                
                #direction vers le bas
                if direction == 'bas':
                        #On déplace le perso de 5 pixel sur l'axe y
                        self.y += 5
                        #Changement de l'image de base
                        self.direction = self.bas
                        
                        #direction vers le haut
                if direction == 'haut':
                        #On déplace le perso de -5 pixel sur l'axe y
                        self.y -= 5
                        #Changement de l'image de base
                        self.direction = self.haut
                        
                        #direction vers la gauche
                if direction == 'gauche':
                        #On déplace le perso de -5 pixel sur l'axe x
                        self.x -= 5
                        #Changement de l'image de base
                        self.direction = self.gauche
                        
                        #direction vers la droite
                if direction == 'droite':
                        #On déplace le perso de 5 pixel sur l'axe x
                        self.x += 5
                        #Changement de l'image de base
                        self.direction = self.droite
		
		
		
		
		
		
		
		

                

	


      		
		
		
			
			
		
		
		
			

         	
