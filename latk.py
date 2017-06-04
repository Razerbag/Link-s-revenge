import pygame
from pygame.locals import * 
from constantes import *

class Latk:


    def __init__(self, droite, gauche, niveau):


        self.droite = pygame.image.load(droite).convert_alpha()

        self.gauche = pygame.image.load(gauche).convert_alpha()

               



        self.direction = self.droite


        self.niveau = niveau

    

    

    def pos(self, ldirection, lx, ly):
        if ldirection == 'droite':
            self.direction = self.droite
            self.box_x = lx +1
            self.box_y = ly
            self.x = self.box_x * taille_img
            self.y = self.box_y * taille_img

            #on place l'atk a cote du perso en fonction de la direction

            
        if ldirection == 'gauche':
            self.direction = self.gauche
            self.box_x = lx -1
            self.box_y = ly
            self.x = self.box_x * taille_img
            self.y = self.box_y * taille_img

            
