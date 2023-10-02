import pygame
from pygame import gfxdraw

MAPVIEW = "mapV"
ROOMVIEW = "roomV"
STARTVIEW = "start"

LEFT="a"
RIGHT="d"
UP="w"
DOWN="s"

MOVETOOL = "move"
EXPANDTOOL = "expand"

def aaCircle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, int(x), int(y), int(radius), color)
    gfxdraw.filled_circle(surface, int(x), int(y), int(radius), color)
    return surface