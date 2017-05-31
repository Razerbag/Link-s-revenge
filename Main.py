#importation du module
import pygame
from pygame.locals import *
from constantes import *
from niveau import *
from perso import *
from mob import *


#initialise toute la bibliothèque
pygame.init()










#création des différents sons du jeu
##truc = pygame.mixer.Sound("")


#Lancement de la musique du jeu

##pygame.mixer.music.load("musique/menu.wav")
##pygame.mixer.music.play()
##
##pygame.mixer.music.set_volume(0.18)

#pygame.mixer.music.load("final.wav")

#BOUCLE DU JEU EN ENTIER


fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
icone = pygame.image.load(image_icone)
pygame.display.set_caption(titre_fenetre)
pygame.display.set_icon(icone)
regles = pygame.image.load(image_regles).convert()
fond = pygame.image.load(image_fond).convert()


roll = 1

while roll:
    
    

    roll_partie = 0
    roll_menu = 1
    roll_regles = 0
    niveau = 0


    while roll_menu:
        menu = pygame.image.load(image_menu).convert()
        fenetre.blit(menu, (0,0))

        pygame.display.flip()

        
        pygame.time.Clock().tick(50)

        for event in pygame.event.get():

           
            if event.type == KEYDOWN:
                #lance le jeu
                 if event.key == K_F1:
                    roll_menu = 0
                    roll_regles = 0
                    roll_partie = 1
                    lvl = 'etage1'

                #lancement des regles du jeu
                 elif event.key == K_F2:
                     roll_menu = 0
                     roll_regles = 1
                     lvl = 0
                     

                     
#stop le jeu
                 elif event.key == K_ESCAPE:
                     
                     roll_menu = 0
                     roll_partie = 0
                     roll = 0
                     lvl = 0

                 
                        
                 elif event.type == QUIT:
                
                     roll_menu = 0
                     roll_partie = 0
                     roll = 0
                     lvl = 0
                     

            
    while roll_regles:
        # regles = pygame.image.load(image_regles).convert()
        fenetre.blit(regles, (0,0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    roll_menu = 1
                    roll_regles = 0                    

                    
                            
                elif event.type == QUIT:
                    pygame.quit()
                    roll = 0
                    

    
    if lvl != 0:

       # fond = pygame.image.load(image_fond).convert()

        clef = 0
        niveau = Niveau(lvl)
        niveau.generation()
        niveau.display(fenetre)


        link = Perso("images/droite.png", "images/gauche.png", "images/haut.png", "images/bas.png", niveau)


    while roll_partie:        

        pygame.time.Clock().tick(60)

    

        for event in pygame.event.get():

        

            if event.type == QUIT:

                roll_partie = 0

                roll = 0

        

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:

                    roll_menu = 0

                    

                

                elif event.key == K_RIGHT:

                    link.move('droite')

                elif event.key == K_LEFT:

                    link.move('gauche')

                elif event.key == K_UP:

                    link.move('haut')

                elif event.key == K_DOWN:

                    link.move('bas')

                elif event.key == K_SPACE:
                    link.atk()

            

        

        fenetre.blit(fond, (0,0))

        niveau.display(fenetre)

        fenetre.blit(link.direction, (link.x, link.y)) 

        pygame.display.flip()


        
        if niveau.etage[link.box_y][link.box_x] == 'c':
            
            clef = 1
            
            
        if niveau.etage[link.box_y][link.box_x] == 'a' and clef == 1:

            roll_partie = 0


pygame.quit()        
