import os 
import random 
import math
import pygame
from os import listdir 
from os.path import isfile, join 
pygame.init()

pygame.display.set_caption("platformer")


BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 800

FPS = 60
PLAYER_VEL = 5

