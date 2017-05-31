import pygame
from pygame.locals import * 
from constantes import *



class Perso:


    def __init__(self, droite, gauche, haut, bas, niveau,):


        self.droite = pygame.image.load(droite).convert_alpha()

        self.gauche = pygame.image.load(gauche).convert_alpha()

        self.haut = pygame.image.load(haut).convert_alpha()

        self.bas = pygame.image.load(bas).convert_alpha()

        

##        self.box_x = 0
##
##        self.box_y = 0
##
##        self.x = 0
##
##        self.y = 0


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
