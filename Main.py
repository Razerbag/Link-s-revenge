import pygame
from pygame.locals import *


pygame.init()

""" valeur """

image_menu = "images/menu.png"

image_fond = "images/fond.jpg"

image_wall = "images/wall.png"

image_welc = "images/welc.png"

image_gate = "images/gate.png"

image_ech = "images/ech.png"

image_plat = "images/plat.png"

image_trou = "images/trou.png"

image_clef =  "images/clef.png"




nombre_img_cote = 15

taille_img = 60

cote_fenetre = nombre_img_cote * taille_img



titre_fenetre = "Link's Revenge"

image_icone = "images/droite.png"






""" function """

class Niveau:


    def __init__(self, fichier):

        self.fichier = fichier

        self.etage = 0

    

    

    def generation(self):


        with open(self.fichier, "r") as fichier:

            etage_niveau = []


            for line in fichier:

                line_niveau = []


                for img in line:


                    if img != '\n':


                        line_niveau.append(img)


                etage_niveau.append(line_niveau)


            self.etage = etage_niveau

    

    

    def display(self, fenetre):


        wall = pygame.image.load(image_wall).convert_alpha()
        welc = pygame.image.load(image_welc).convert_alpha()
        gate = pygame.image.load(image_gate).convert_alpha()
        ech = pygame.image.load(image_ech).convert_alpha()
        plat = pygame.image.load(image_plat).convert_alpha()
        trou = pygame.image.load(image_trou).convert_alpha()
        clef = pygame.image.load(image_clef).convert_alpha()
        


        num_line = 0

        for line in self.etage:


            num_box = 0

            for img in line:


                x = num_box * taille_img

                y = num_line * taille_img

                if img == 'm':          #wall

                    fenetre.blit(wall, (x,y))

                elif img == 'd':        #debut/welc

                    fenetre.blit(welc, (x,y))
                    Perso.box_x = num_box
                    Perso.box_y = num_line
                    Perso.x = num_box * taille_img
                    Perso.y = num_line * taille_img

                elif img == 'a':        #fin/ gate

                    fenetre.blit(gate, (x,y))

                elif img == 'e':   # echelle/ ech

                    fenetre.blit(ech, (x,y))

                elif img == 'p': #plateforme

                    fenetre.blit(plat, (x,y))

                elif img == 't': #trou(plateforme/echelle)

                    fenetre.blit(trou, (x,y))

                elif img == 'c': #clef

                    fenetre.blit(clef, (x,y))

                num_box += 1

            num_line += 1

            

            

            

            

class Perso:


    def __init__(self, droite, gauche, haut, bas, niveau,):


        self.droite = pygame.image.load(droite).convert_alpha()

        self.gauche = pygame.image.load(gauche).convert_alpha()

        self.haut = pygame.image.load(haut).convert_alpha()

        self.bas = pygame.image.load(bas).convert_alpha()

        



        self.direction = self.droite


        self.niveau = niveau

    

    

    def move(self, direction):


        


        if direction == 'droite':


            if self.box_x < (nombre_img_cote - 1):


                if self.niveau.etage[self.box_y][self.box_x+1] == '0':

                    self.box_x += 1

                    self.x = self.box_x * taille_img

                elif self.niveau.etage[self.box_y][self.box_x+1] == 'd':

                    self.box_x += 1

                    self.x = self.box_x * taille_img

                elif self.niveau.etage[self.box_y][self.box_x+1] == 'a':

                    self.box_x += 1

                    self.x = self.box_x * taille_img

                elif self.niveau.etage[self.box_y][self.box_x+1] == 'e':

                    self.box_x += 1

                    self.x = self.box_x * taille_img

                elif self.niveau.etage[self.box_y][self.box_x+1] == 'c':

                    self.box_x += 1

                    self.x = self.box_x * taille_img


            self.direction = self.droite

        


        if direction == 'gauche':

            if self.box_x > 0:

                if self.niveau.etage[self.box_y][self.box_x-1] == '0':

                    self.box_x -= 1

                    self.x = self.box_x * taille_img
                    

                elif self.niveau.etage[self.box_y][self.box_x-1] == 'd':

                    self.box_x -= 1

                    self.x = self.box_x * taille_img
                    

                elif self.niveau.etage[self.box_y][self.box_x-1] == 'a':

                    self.box_x -= 1

                    self.x = self.box_x * taille_img
                    

                elif self.niveau.etage[self.box_y][self.box_x-1] == 'e':

                    self.box_x -= 1

                    self.x = self.box_x * taille_img

                elif self.niveau.etage[self.box_y][self.box_x-1] == 'c':

                    self.box_x -= 1

                    self.x = self.box_x * taille_img

                    

            self.direction = self.gauche

        


        if direction == 'haut':
            if self.box_y > 0:

                if self.niveau.etage[self.box_y-1][self.box_x] == 't':

                    self.box_y -= 1

                    self.y = self.box_y * taille_img

                if self.niveau.etage[self.box_y-1][self.box_x] == 'e':

                    self.box_y -= 1

                    self.y = self.box_y * taille_img

            self.direction = self.haut

        


        if direction == 'bas':

            if self.box_y < (nombre_img_cote - 1):

                if self.niveau.etage[self.box_y+1][self.box_x] == 't':

                    self.box_y += 1

                    self.y = self.box_y * taille_img

                elif self.niveau.etage[self.box_y+1][self.box_x] == 'e':

                    self.box_y += 1

                    self.y = self.box_y * taille_img
                

            self.direction = self.bas
            
#gravity
        while self.niveau.etage[self.box_y+1][self.box_x] == '0':
            
            self.box_y  +=  1
            self.y = self.box_y * taille_img
            continue
        if self.niveau.etage[self.box_y+1][self.box_x] == 'a':
            self.box_y  +=  1
            self.y = self.box_y * taille_img
        elif self.niveau.etage[self.box_y+1][self.box_x] == 'c':
            self.box_y  +=  1
            self.y = self.box_y * taille_img


""" prog """


fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
icone = pygame.image.load(image_icone)
pygame.display.set_caption(titre_fenetre)
pygame.display.set_icon(icone)


roll = 1

while roll:
    
    menu = pygame.image.load(image_menu).convert()
    fenetre.blit(menu, (0,0))

    pygame.display.flip()

    roll_partie = 1
    roll_menu = 1


    while roll_menu:
        pygame.time.Clock().tick(50)

        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == K_F1:

                    roll_menu = 0   

                    lvl = 'etage1'        

                

                elif event.key == K_2 and event.key == K_RETURN:

                    roll_menu = 0

                    lvl = 'boss'
                    
            elif event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
                
                roll_menu = 0
                roll_partie = 0
                roll = 0
                lvl = 0



    if lvl != 0:

        fond = pygame.image.load(image_fond).convert()

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
        
