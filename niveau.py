import pygame
from pygame.locals import * 
from constantes import *
from perso import *
from mob import *


#creation de l'objet niveau
class Niveau:


    def __init__(self, fichier): #on attribut a l'obj, self et le fichier du niveau

        self.fichier = fichier #l'obj niveau prend une variable appelé fichier dans laquelle on met le fichier du niveau à chargé

        self.etage = 0 

    

    

    def generation(self, clef):

        


        with open(self.fichier, "r") as fichier: # on lit le fichier du niveau à charger

            etage_niveau = [] #on crée un espace de stockage dans lequel nous allons mettre les  informations de construction de l'etage


            for line in fichier: #pour chaque etape horizontal de l'etage on crée un liste contenant chaque elements de la ligne  

                line_niveau = []


                for img in line:


                    if img != '\n':

                        if img != 'c':

                            line_niveau.append(img)
                            
                        if img == 'c' and clef != 1:
                            line_niveau.append(img)
                        if img == 'c' and clef == 1:
                            line_niveau.append('0')


                etage_niveau.append(line_niveau)


            self.etage = etage_niveau #on enregistre 

    

    

    def display(self, fenetre):


        wall = pygame.image.load(image_wall).convert_alpha()
        welc = pygame.image.load(image_welc).convert_alpha()
        gate = pygame.image.load(image_gate).convert_alpha()
        ech = pygame.image.load(image_ech).convert_alpha()
        plat = pygame.image.load(image_plat).convert_alpha()
        trou = pygame.image.load(image_trou).convert_alpha()
        clef = pygame.image.load(image_clef).convert_alpha()
        


        num_line = 0

        for line in self.etage:#on parcourt notre espace stockant les lignes


            num_box = 0

            for img in line:#on lit ligne apres ligne


                x = num_box * taille_img #adapte une box à la taille des image

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

                elif img == 't': #trou(plateforme/echelle)s

                    fenetre.blit(trou, (x,y))

                elif img == 'c':
                    
                    fenetre.blit(clef, (x,y))
                    mob.box_x = num_box
                    mob.box_y = num_line
                    mob.x = num_box * taille_img
                    mob.y = num_line * taille_img
                    
                

                num_box += 1

            num_line += 1
