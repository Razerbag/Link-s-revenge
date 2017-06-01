#importation du module et des autres branches
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

#ouverture de la fenetre, titre, icone
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

icone = pygame.image.load(image_icone)
pygame.display.set_caption(titre_fenetre)
pygame.display.set_icon(icone)

#chargement au préalable des deux fonds utiliser dans le menu
regles = pygame.image.load(image_regles).convert()
fond = pygame.image.load(image_fond).convert()

#lancement de la boucle principale
roll = 1
clef = 0

while roll:
    
    
#prepare les differentes boucles, lancement de la boucle du menu
    roll_partie = 0
    roll_menu = 1
    roll_regles = 0
    niveau = 0
    


    while roll_menu:
        #affichage de l'acceuil
        menu = pygame.image.load(image_menu).convert()
        fenetre.blit(menu, (0,0))

        pygame.display.flip()

        #limitation de vitesse
        pygame.time.Clock().tick(100)

#attente d'une action utilisateur
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
                     

#affiche des regles du jeu            
    while roll_regles:
        fenetre.blit(regles, (0,0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    roll_menu = 1
                    roll_regles = 0                    

                    
                            
                elif event.type == QUIT:
                    pygame.quit()
                    roll_regles = 0
                    roll = 0
                    

    #intialisation du jeu
    if lvl != 0:



        clef = 0
        niveau = Niveau(lvl) #initialisation du niveau
        niveau.generation() #generation du niveau
        niveau.display(fenetre)  #affichage du niv genere


        link = Perso("images/droite.png", "images/gauche.png", "images/haut.png", "images/bas.png", niveau)
#initialisation du personnage

    while roll_partie:        

        pygame.time.Clock().tick(60)

    #attente d'une action utilisateur

        for event in pygame.event.get():

        

            if event.type == QUIT:

                roll_partie = 0

                roll = 0

        

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:

                    roll_menu = 0

                    

                

                elif event.key == K_RIGHT:    #si demande de deplacement de l'utilisateurs, lance la fonction de mouvement associé

                    link.move('droite')

                elif event.key == K_LEFT:

                    link.move('gauche')

                elif event.key == K_UP:

                    link.move('haut')

                elif event.key == K_DOWN:

                    link.move('bas')

                elif event.key == K_SPACE:
                    link.atk()

            


        

        fenetre.blit(fond, (0,0)) #remet le fond

        niveau.display(fenetre) #on remet le niveau

        fenetre.blit(link.direction, (link.x, link.y)) #on remet link à sa nouvelle position

        pygame.display.flip() #actuallisation de la fenetre


        
        if niveau.etage[link.box_y][link.box_x] == 'c': #on verifie si link est sur la case de la clef
            
            clef = 1 #on le note
            fenetre.blit(fond, (0,0)) #remet le fond

            niveau.display(fenetre) #on remet le niveau

            fenetre.blit(link.direction, (link.x, link.y)) #on remet link à sa nouvelle position

            pygame.display.flip()#on retire 
            
            
            
        if niveau.etage[link.box_y][link.box_x] == 'a' and clef == 1: #on verifie si link est sur la case de la fin et si il a la clef

            roll_partie = 0


pygame.quit()        
