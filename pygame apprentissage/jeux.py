#script jeu video test

import os, sys, pygame
from pygame.locals import *
#import Camera, maps
from Classes import *


pygame.init()

#cam = Camera()
#map_s = pygame.sprite.Group()
        

#cam.set(arii.x, arii.y)

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800,600))

#Icone
icone = pygame.image.load("icone.jpg")
pygame.display.set_icon(icone)

#Titre
titre_fenetre = ("Pykemon")
pygame.display.set_caption(titre_fenetre)

continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load("imageaccueil.png").convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				
				
				
			elif event.type == KEYDOWN:
                                
				if event.key == K_F1:
                                        continuer_accueil = 0
                                        fond = pygame.image.load("map.png").convert()
                                        fenetre.blit(fond, (0,0))
                                        arii = Perso("droite.png","gauche.png","haut.png","bas.png")
                                        pygame.key.set_repeat(400, 50)
                                        pygame.display.flip()
        
        #BOUCLE JEU
	while continuer_jeu:
                
                pygame.time.Clock().tick(30)
                
                for event in pygame.event.get():
                        
                        if event.type == QUIT:
                                
                                continuer_jeu = 0
                                continuer = 0
                        
                        elif event.type == KEYDOWN:
                                
                                if event.key == K_F4:
                                        fenetre = pygame.display.set_mode((640,480),pygame.FULLSCREEN)
                                elif event.key == K_ESCAPE:
                                        fenetre = pygame.display.set_mode((640,480))
                                elif event.key == K_RIGHT:
                                        arii.deplacer('droite')
                                elif event.key == K_LEFT:
                                        arii.deplacer('gauche')    
                                elif event.key == K_UP:
                                        arii.deplacer('haut')
                                elif event.key == K_DOWN:
                                        arii.deplacer('bas')
                                        
                #cam.set (arii.x, arii.y)
                fenetre.blit(fond, (0,0))
                #map_s.update(cam.x, cam.y)
                #map_s.draw(fenetre)
                fenetre.blit(arii.direction, (arii.x, arii.y))
                pygame.display.flip()

     
                                

