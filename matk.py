import pygame
from pygame.locals import * 
from constantes import *

class Matk:


    def __init__(self, droite, gauche, niveau):


        self.droite = pygame.image.load(droite).convert_alpha()

        self.gauche = pygame.image.load(gauche).convert_alpha()

               



        self.direction = self.droite


        self.niveau = niveau

    

    

    def pos(self, mdirection, mx, my):
        if mdirection == 'droite':
            self.direction = self.droite
            self.box_x = mx +1
            self.box_y = my
            self.x = self.box_x * taille_img
            self.y = self.box_y * taille_img

            
        if mdirection == 'gauche':
            self.direction = self.gauche
            self.box_x = mx -1
            self.box_y = my
            self.x = self.box_x * taille_img
            self.y = self.box_y * taille_img

            
