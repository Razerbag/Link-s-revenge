#importation du module et des autres branches
import pygame
from random import *
from pygame.locals import *
from constantes import *
from niveau import *
from perso import *
from mob import *
from latk import *
from matk import *


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


#initialisation de futur variable
tps_latk = pygame.time.get_ticks() 
tps_matk = pygame.time.get_ticks() 
mob1_atk_tps = pygame.time.get_ticks()


 #lancement de la boucle principale
roll = 1



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

        
#attente d'une action utilisateur
        for event in pygame.event.get():

           
            if event.type == KEYDOWN:
                #lance le jeu
                 if event.key == K_F1:
                    roll_menu = 0
                    roll_regles = 0
                    roll_partie = 1
                    lvl = 'etage1'
                    clef = 0

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
                    
                elif event.key == K_F1:
                    roll_menu = 0
                    roll_regles = 0
                    roll_partie = 1
                    lvl = 'etage1'
                    
                            
                elif event.type == QUIT:
                    pygame.quit()
                    roll_regles = 0
                    roll = 0
                    




    #intialisation du jeu
    if lvl == 'etage1':
        
        niveau = Niveau(lvl) #initialisation du niveau
        niveau.generation(clef) #generation du niveau
        niveau.display(fenetre)  #affichage du niv genere

        
        link = Perso("images/droite.png", "images/gauche.png", "images/haut.png", "images/bas.png", niveau) #link
        latk = Latk("images/latkdroite.png", "images/latkgauche.png", niveau) #atk link
        ldirection = 'droite'
        link_vie = 3
        
#initialisation du personnage
        
        mob1 = mob("images/mobdroite.png", "images/mobgauche.png", niveau)#mob        
        matk = Matk("images/matkdroite.png", "images/matkgauche.png", niveau) #atk de mob
        mob1.box_x = 8
        mob1.box_y = 8
        mob1.x = 8 * taille_img
        mob1.y = 8 * taille_img
        roll_mob1 = 1
        mob1_act  = pygame.time.get_ticks() + randint(300,600)
        mob1_vie = 2
        mdirection = 'droite'
#initialisation du mob1
        latk.x, latk.y = cote_fenetre, cote_fenetre
        matk.x, matk.y = 8, 8
        #preparation atk





    while roll_partie:
            #attente d'une action utilisateur            
        for event in pygame.event.get():

        

            if event.type == QUIT:

                roll_partie = 0

                roll = 0

        

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:

                    roll_menu = 0

                    

                

                elif event.key == K_RIGHT:    #si demande de deplacement de l'utilisateurs, lance la fonction de mouvement associé
                    ldirection = 'droite'
                    link.move('droite')

                elif event.key == K_LEFT:
                    ldirection = 'gauche'
                    link.move('gauche')

                elif event.key == K_UP:

                    link.move('haut')

                elif event.key == K_DOWN:

                    link.move('bas')

                elif event.key == K_e: #atk de link 
                    Latk.pos(latk, ldirection, link.box_x, link.box_y) #fait appel à l objet  
                    
                    fenetre.blit(latk.direction, (latk.x, latk.y))
                    pygame.display.flip()
                    if mob1.x == latk.x and mob1.y == latk.y:
                        
                        mob1_vie -= 1
                        
                    tps_latk = pygame.time.get_ticks() + 200

                    
                    
        if pygame.time.get_ticks() >= tps_latk:
            Latk.pos(latk, ldirection, 15, 15)
            fenetre.blit(fond, (0,0))
            niveau.display(fenetre)
            fenetre.blit(link.direction, (link.x, link.y)) 
            fenetre.blit(latk.direction, (latk.x, latk.y))
            if mob1_vie != 0:
                fenetre.blit(mob1.direction, (mob1.x, mob1.y))
                fenetre.blit(matk.direction, (matk.x, matk.y))
            pygame.display.flip()


            
            

        
        if pygame.time.get_ticks() >= mob1_act: #variation aleat de la position du mob, ou uniquement ça direction(tdroite tgauche)while roll_mob1: #variation aleat de la position du mob, ou uniquement ça direction(tdroite tgauche)
            
            if link.box_y != mob1.box_y:
                orie = randint(1,25) 
                if orie <= 8:
                    mob1.move('droite')
                    mdirection = 'droite'

                elif orie > 8 and orie <= 16:
                    mob1.move('gauche')
                    mdirection = 'gauche'

                elif orie > 16 and orie <= 20:
                    mob1.move('tdroite')
                    mdirection = 'droite'

                elif orie > 20 and orie <= 24:
                    mob1.move('tgauche')
                    mdirection = 'gauche'


                    

            elif link.box_y == mob1.box_y:

                
                if link.box_x < mob1.box_x:
                    mob1.move('tgauche')
                    mdirection = 'gauche'




                    

                if link.box_x > mob1.box_x:
                    mob1.move('tdroite')
                    mdirection = 'droite'
                    




                    
            mob1_act  += randint(900,1400)

        if pygame.time.get_ticks() >= mob1_atk_tps:
            Matk.pos(matk, mdirection, mob1.box_x, mob1.box_y)                    
            fenetre.blit(matk.direction, (matk.x, matk.y))
            if link.x == matk.x and link.y == matk.y:
                pygame.time.Clock().tick(250)
                link_vie -= 1
            pygame.display.flip()
            
            mob1_atk_tps = pygame.time.get_ticks() + 985 #temps restant avant prochaine atk
            tps_matk = pygame.time.get_ticks() + 200 #temps restant avant supp image atk

        if pygame.time.get_ticks() >= tps_matk:
            Matk.pos(matk, mdirection, 15, 15)
            fenetre.blit(fond, (0,0))
            niveau.display(fenetre)
            fenetre.blit(link.direction, (link.x, link.y)) 
            fenetre.blit(latk.direction, (latk.x, latk.y))
            
            if mob1_vie != 0:
                fenetre.blit(mob1.direction, (mob1.x, mob1.y))
                fenetre.blit(matk.direction, (matk.x, matk.y))
                
            pygame.display.flip()


        if pygame.time.get_ticks() >= tps_latk:
            Latk.pos(latk, ldirection, 15, 15)
            fenetre.blit(fond, (0,0))
            niveau.display(fenetre)
            fenetre.blit(link.direction, (link.x, link.y)) 
            fenetre.blit(latk.direction, (latk.x, latk.y))
            
            if mob1_vie != 0:
                fenetre.blit(mob1.direction, (mob1.x, mob1.y))
                fenetre.blit(matk.direction, (matk.x, matk.y))

            
            pygame.display.flip()
        


            

            


            


        
        
        fenetre.blit(fond, (0,0)) #remet le fond

        niveau.display(fenetre) #on remet le niveau
                                #on remet link à sa nouvelle position
        fenetre.blit(link.direction, (link.x, link.y)) 
        fenetre.blit(latk.direction, (latk.x, latk.y))
        if mob1_vie != 0:
            fenetre.blit(mob1.direction, (mob1.x, mob1.y))
            fenetre.blit(matk.direction, (matk.x, matk.y))
        pygame.display.flip() #actuallisation de la fenetre
        


            
            
        
        if link_vie == 0:
            roll_partie = 0
           # roll_perdu = 1

            
        if niveau.etage[link.box_y][link.box_x] == 'c': #on verifie si link est sur la case de la clef
            clef = 1 #on le note
            fenetre.blit(fond, (0,0)) #remet le fond
            niveau = Niveau(lvl) #initialisation du niveau
            niveau.generation(clef) #generation du niveau sans la clef
        
            niveau.display(fenetre) #on remet le niveau

            fenetre.blit(link.direction, (link.x, link.y)) 
            fenetre.blit(latk.direction, (latk.x, latk.y))
            
            if mob1_vie != 0:
                fenetre.blit(mob1.direction, (mob1.x, mob1.y))
                fenetre.blit(matk.direction, (matk.x, matk.y))
           

            pygame.display.flip() #actualisation
          
            
            
            
        if niveau.etage[link.box_y][link.box_x] == 'a' and clef == 1: #on verifie si link est sur la case de la fin et si il a la clef

            roll_partie = 0


pygame.quit()        
