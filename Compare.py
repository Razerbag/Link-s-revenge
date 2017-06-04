import pygame
from pygame.locals import * 
from constantes import *





class mob:


    def __init__(self, droite, gauche, niveau):


        self.droite = pygame.image.load(droite).convert_alpha()

        self.gauche = pygame.image.load(gauche).convert_alpha()

               



        self.direction = self.droite


        self.niveau = niveau

    

    

    def move(self, direction):


        

        if direction == 'tdroite':
            self.direction = self.droite
        if direction == 'tgauche':
            self.direction = self.gauche
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

      
                

            
            
