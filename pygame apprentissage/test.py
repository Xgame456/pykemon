#script jeu video test

import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640,480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)
pygame.key.set_repeat(400, 50)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        
                if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				fentre = pygame.display.set_mode((640,480))
			if event.key == K_F4:
				fenetre = pygame.display.set_mode((640,480),pygame.FULLSCREEN)
                        if event.key == K_RIGHT:
                                position_perso = position_perso.move(3,0)
                        if event.key == K_LEFT:
                                position_perso = position_perso.move(-3,0)
                        if event.key == K_UP:
                                position_perso = position_perso.move(0, -3)
                        if event.key == K_DOWN:
                                position_perso = position_perso.move(0,3)
	





                
        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position_perso)
        pygame.display.flip()
