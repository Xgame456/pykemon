#script jeu video test

import os, sys, pygame
from pygame.locals import *
import Camera, maps
from Classes import *


pygame.init()

#cam = Camera()
#map_s = pygame.sprite.Group()
        

#cam.set(arii.x, arii.y)

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((500,400))

#Icone
icone = pygame.image.load("icone.jpg").convert()
pygame.display.set_icon(icone)

#Titre
titre_fenetre = ("Pykemon")
pygame.display.set_caption(titre_fenetre)

#Chargement et collage du fond
fond = pygame.image.load("map.png").convert()
fenetre.blit(fond, (0,0))

#Chargement du personnage
arii = Perso("droite.png","gauche.png","haut.png","bas.png")
pygame.key.set_repeat(400, 50)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        
                elif event.type == KEYDOWN:
                        if event.key == K_F4:
                                fenetre = pygame.display.set_mode((640,480),pygame.FULLSCREEN)
                        if event.key == K_ESCAPE:
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
                                
main()


                
       
