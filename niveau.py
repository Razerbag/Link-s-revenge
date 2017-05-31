import pygame
from pygame.locals import * 
from constantes import *
from perso import *
from mob import *

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
