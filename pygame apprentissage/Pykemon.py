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
        accueil = pygame.image.load("accueil.jpg").convert()
        fenetre.blit(accueil, (0,0))
        pygame.display.flip()
        continuer_jeu = 1
        continuer_accueil = 1
        
        while continuer_accueil:
                pygame.time.Clock().tick(30)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                        elif event.type == KEYDOWN:
                                if event.key == K_F1:
                                        pygame.display.flip()
                                        continuer_accueil = 0
                                        choix = 1
                                        fenetre.fill((0,0,0))
                                        fond = pygame.image.load("map.png").convert()
                                        fenetre.blit(fond, (0,0))
                           
        while choix :
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                
                        elif event.type == KEYDOWN:
                                if event.key == K_DOWN:
                                        arii.deplacer('bas')
                                elif event.key == K_UP:
                                        arii.deplacer('haut')
                                
                                elif event.key == K_LEFT:
                                        arii.deplacer('gauche')
                                        
                                elif event.key == K_RIGHT:
                                        arii.deplacer('droite')
                                        
                                if event.key == K_ESCAPE:
                                        fenetre = pygame.display.set_mode((800,600))
                                        
                                if event.key == K_F4:
                                        fenetre = pygame.display.set_mode((800,600),pygame.FULLSCREEN)
                                
                      
                                
                                                
                                
                       
                if arii.x > 500 and arii.x < 800 and arii.y >300 and arii.y < 527:
                        fond = pygame.image.load("background.Jpg").convert()
                fenetre.fill((0,0,0))
                fenetre.blit(fond, (0,0))
                fenetre.blit(arii.direction, (arii.x, arii.y))
                fenetre.blit(téléportation, (500, 300))
                pygame.display.flip()
       
                
               
                
        
                                
