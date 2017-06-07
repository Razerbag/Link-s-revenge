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
fenetre = pygame.display.set_mode((cote_fenetre, haut_fenetre))
icone = pygame.image.load(image_icone)
pygame.display.set_caption(titre_fenetre)
pygame.display.set_icon(icone)


#chargement au préalable des deux fonds utiliser dans le menu
regles = pygame.image.load(image_regles).convert()
fond = pygame.image.load(image_fond).convert()


#initialisation de futur variable
tps_latk = pygame.time.get_ticks() +100
tps_matk = pygame.time.get_ticks() +100
tps_matk2 = pygame.time.get_ticks() +100
tps_matk3 = pygame.time.get_ticks() +100
mob1_atk_tps = pygame.time.get_ticks() +100
mob2_atk_tps = pygame.time.get_ticks() +100
mob3_atk_tps = pygame.time.get_ticks() +100
#mob.x, mob.y, mob.x2, mob.y2, mob.x3, mob.y3 = cote_fenetre, haut_fenetre, cote_fenetre, haut_fenetre, cote_fenetre, haut_fenetre


 #lancement de la boucle principale
roll = 1

def actu():
    niveau = Niveau(lvl) #initialisation du niveau
    niveau.generation(clef) #generation du niveau
    niveau.display(fenetre)  #affichage du niv genere               
    fenetre.blit(fond, (0,0))
    niveau.display(fenetre)
    fenetre.blit(link.direction, (link.x, link.y)) 
    fenetre.blit(latk.direction, (latk.x, latk.y))
    if mob1_vie != 0:
        fenetre.blit(mob1.direction, (mob1.x, mob1.y))
        fenetre.blit(matk.direction, (matk.x, matk.y))
    if mob2_vie != 0:
        fenetre.blit(mob2.direction, (mob2.x2, mob2.y2))
        fenetre.blit(matk2.direction, (matk2.x2, matk2.y2))        
    if mob3_vie != 0:
        fenetre.blit(mob3.direction, (mob3.x3, mob3.y3))
        fenetre.blit(matk3.direction, (matk3.x3, matk3.y3))
    pygame.display.flip()

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
                    clef = 0
                    
                            
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
        mob1_act  = pygame.time.get_ticks() + randint(300,600)
        mob1_vie = 2
        mdirection = 'droite'
#initialisation du mob1

        mob2 = mob("images/mobdroite.png", "images/mobgauche.png", niveau)#mob        
        matk2 = Matk("images/matkdroite.png", "images/matkgauche.png", niveau) #atk de mob
        mob2_act  = pygame.time.get_ticks() + randint(300,600)
        mob2_vie = 3
        m2direction = 'droite'
#initialisation du mob1

        mob3 = mob("images/mobdroite.png", "images/mobgauche.png", niveau)#mob        
        matk3 = Matk("images/matkdroite.png", "images/matkgauche.png", niveau) #atk de mob
        mob3_act  = pygame.time.get_ticks() + randint(300,600)
        mob3_vie = 2
        m3direction = 'droite'
#initialisation du mob1

        mob1.x
        latk.x, latk.y = cote_fenetre, haut_fenetre
        matk.x, matk.y = cote_fenetre, haut_fenetre
        matk2.x2, matk2.y2 = cote_fenetre, haut_fenetre
        matk3.x3, matk3.y3 = cote_fenetre, haut_fenetre
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
                    if mob2.x2 == latk.x and mob2.y2 == latk.y:
                        
                        mob2_vie -= 1
                    if mob3.x3 == latk.x and mob3.y3 == latk.y:
                        
                        mob3_vie -= 1
                        
                    tps_latk = pygame.time.get_ticks() + 200

                    
                    
        if pygame.time.get_ticks() >= tps_latk:
            Latk.pos(latk, ldirection, 13, 25)
            actu()


            
            

        
        if pygame.time.get_ticks() >= mob1_act: #variation aleat de la position du mob, ou uniquement ça direction(tdroite tgauche)while roll_mob1: #variation aleat de la position du mob, ou uniquement ça direction(tdroite tgauche)
            
            if link.box_y != mob1.box_y:
                orie = randint(1,25) 
                if orie <= 8:
                    mob1.move('droite', 1)
                    mdirection = 'droite'

                elif orie > 8 and orie <= 16:
                    mob1.move('gauche', 1)
                    mdirection = 'gauche'

                elif orie > 16 and orie <= 20:
                    mob1.move('tdroite', 1)
                    mdirection = 'droite'

                elif orie > 20 and orie <= 24:
                    mob1.move('tgauche', 1)
                    mdirection = 'gauche'
                   

            elif link.box_y == mob1.box_y:

                
                if link.box_x < mob1.box_x:
                    mob1.move('tgauche', 1)
                    mdirection = 'gauche'
                   

                if link.box_x > mob1.box_x:
                    mob1.move('tdroite', 1)
                    mdirection = 'droite'
                    
            mob1_act  += randint(900,1400)


            

        if pygame.time.get_ticks() >= mob2_act: #action du mob 2
            
            if link.box_y != mob2.box_y2:
                orie = randint(1,25) 
                if orie <= 8:
                    mob2.move('droite', 2)
                    m2direction = 'droite'

                elif orie > 8 and orie <= 16:
                    mob2.move('gauche', 2)
                    m2direction = 'gauche'

                elif orie > 16 and orie <= 20:
                    mob2.move('tdroite', 2)
                    m2direction = 'droite'

                elif orie > 20 and orie <= 24:
                    mob2.move('tgauche', 2)
                    m2direction = 'gauche'
                    

            elif link.box_y == mob2.box_y2:

                
                if link.box_x < mob2.box_x2:
                    mob2.move('tgauche', 2)
                    m2direction = 'gauche'
                   

                if link.box_x > mob2.box_x2:
                    mob2.move('tdroite', 2)
                    m2direction = 'droite'                   

            mob2_act  += randint(900,1400)

            

        if pygame.time.get_ticks() >= mob3_act: #action du mob 3
            
            if link.box_y != mob3.box_y3:
                orie = randint(1,25) 
                if orie <= 8:
                    mob3.move('droite', 3)
                    m3direction = 'droite'

                elif orie > 8 and orie <= 16:
                    mob3.move('gauche', 3)
                    m3direction = 'gauche'

                elif orie > 16 and orie <= 20:
                    mob3.move('tdroite', 3)
                    m3direction = 'droite'

                elif orie > 20 and orie <= 24:
                    mob3.move('tgauche', 3)
                    m3direction = 'gauche'



            elif link.box_y == mob3.box_y3:
                
                
                if link.box_x < mob3.box_x3:
                    mob3.move('tgauche', 3)
                    m3direction = 'gauche'
                   

                if link.box_x > mob3.box_x3:
                    mob3.move('tdroite', 3)
                    m3direction = 'droite'          

                    
            mob3_act  += randint(900,1400)


            
        if mob1_vie != 0:
            if pygame.time.get_ticks() >= mob1_atk_tps:
                Matk.pos(matk, mdirection, mob1.box_x, mob1.box_y, 1)                    
                fenetre.blit(matk.direction, (matk.x, matk.y))
                if link.x == matk.x and link.y == matk.y:
                    pygame.time.Clock().tick(250)
                    link_vie -= 1
                pygame.display.flip()
                
                mob1_atk_tps = pygame.time.get_ticks() + 985 #temps restant avant prochaine atk
                tps_matk = pygame.time.get_ticks() + 200 #temps restant avant supp image atk
        if mob2_vie != 0:    
            if pygame.time.get_ticks() >= mob2_atk_tps:
                Matk.pos(matk2, m2direction, mob2.box_x2, mob2.box_y2, 2)                    
                fenetre.blit(matk2.direction, (matk2.x2, matk2.y2))
                pygame.display.flip()
                if link.x == matk2.x2 and link.y == matk2.y2:
                    pygame.time.Clock().tick(250)
                    link_vie -= 1
                
                
                mob2_atk_tps = pygame.time.get_ticks() + 985 
                tps_matk2 = pygame.time.get_ticks() + 200 
        if mob3_vie != 0:    
            if pygame.time.get_ticks() >= mob3_atk_tps:
                Matk.pos(matk3, m3direction, mob3.box_x3, mob3.box_y3, 3)                    
                fenetre.blit(matk3.direction, (matk3.x3, matk3.y3))
                pygame.display.flip()
                if link.x == matk3.x3 and link.y == matk3.y3:
                    pygame.time.Clock().tick(250)
                    link_vie -= 1            
            
                mob3_atk_tps = pygame.time.get_ticks() + 985 
                tps_matk3 = pygame.time.get_ticks() + 200 





            
        if pygame.time.get_ticks() >= tps_matk:
            Matk.pos(matk, mdirection, 13, 25, 1)
            actu()

            
        if pygame.time.get_ticks() >= tps_matk2:
            Matk.pos(matk2, m2direction, 13, 25, 2)
            actu()
            
          

        if pygame.time.get_ticks() >= tps_matk3:
            Matk.pos(matk3, m3direction, 13, 25, 3)
            actu()



            


        if pygame.time.get_ticks() >= tps_latk:
            Latk.pos(latk, ldirection, 13, 25)
            actu()
        
          

            


            


        
        
        actu()
        


            
            
        
        if link_vie == 0:
            roll_partie = 0
           # roll_perdu = 1

            
        if niveau.etage[link.box_y][link.box_x] == 'c': #on verifie si link est sur la case de la clef
            clef = 1 #on le note
            fenetre.blit(fond, (0,0)) #remet le fond
            niveau = Niveau(lvl) #initialisation du niveau
            niveau.generation(clef) #generation du niveau sans la clef
        
            actu()
          
            
            
            
        if niveau.etage[link.box_y][link.box_x] == 'a' and clef == 1: #on verifie si link est sur la case de la fin et si il a la clef

            roll_partie = 0


pygame.quit()        
