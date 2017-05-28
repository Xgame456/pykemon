#script jeu video test

import pygame
from pygame.locals import *

from Classes import *


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800, 600))

#Icone
icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)

#Titre
titre_fenetre = ("Pykemon")
pygame.display.set_caption(titre_fenetre)

#Chargement et collage du fond
fond = pygame.image.load("map.png").convert()
fenetre.blit(fond, (0,0))

#Chargement du personnage
arii = Perso("droite.png","gauche.png","haut.png","bas.png")
#Chargement du portail
téléportation = pygame.image.load("portail.png").convert()

#Rafraîchissement de l'écran
pygame.display.flip()

#Répétition de la touche du clavier
pygame.key.set_repeat(400, 30)

#BOUCLE INFINIE
continuer = 1
while continuer:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
                #Si on clique sur la croix, pygame quitte.
                if event.type == QUIT:
                        pygame.quit()
                        
                #On attente qu'un touche spécifique du clavier soit présser
                elif event.type == KEYDOWN:
                        
                        #Si la touche F4 est présser le jeu passe en plein écran
                        if event.key == K_F4:
                                fenetre = pygame.display.set_mode((640,480),pygame.FULLSCREEN)
                                
                        #Si la touche Echap est présser le jeu revien an l'écran normal
                        if event.key == K_ESCAPE:
                                fenetre = pygame.display.set_mode((640,480))
                                
                        #Si la fleche de droite est appuyer, le perso se déplace vers la droite
                        elif event.key == K_RIGHT:
                                arii.deplacer('droite')
                                
                        #Si la fleche de gauche est appuyer, le perso se déplace vers la gauche
                        elif event.key == K_LEFT:
                                arii.deplacer('gauche')
                                
                        #Si la fleche du haut est appuyer, le perso se déplace vers le haut
                        elif event.key == K_UP:
                                arii.deplacer('haut')
                                
                        #Si la fleche du bas est appuyer, le perso se déplace vers le bas
                        elif event.key == K_DOWN:
                                arii.deplacer('bas')
        #délimitation d'une zone                       
        if arii.x > 500 and arii.x < 800 and arii.y >300 and arii.y < 527:
                
                #Si arii est dans la zonne l'arriere plan du jeu change
                fond = pygame.image.load("background.Jpg").convert()
                
        #On efface l'ancien arriere plan
        fenetre.fill((0,0,0))
        
        #On "colle" l'arriere plan
        fenetre.blit(fond, (0,0))
        
        #On colle le perso suivant sa direction
        fenetre.blit(arii.direction, (arii.x, arii.y))
        
        #On colle le portail au coordonnée x=500 et y=300
        fenetre.blit(téléportation, (500, 300))
        
        #rafraichissemnt de l'écran
        pygame.display.flip()
       
                
               
                
        
                                
