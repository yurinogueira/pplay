# Pygame and system modules
import pygame
from pygame import RLEACCEL

from pplay.baseobject import BaseRectObject
from pplay.collision import Collision
from pplay.gameobject import GameObject
from pplay.window import Window

# Initializes pygame's modules
pygame.init()


# Loads an image (with colorkey and alpha)
def load_image(name, colorkey=None, alpha=False):
    """loads an image into memory"""
    image = pygame.image.load(name)
    if alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


"""GameImage is the base class to deal with images"""


class GameImage(GameObject, BaseRectObject):
    """
    Creates a GameImage from the specified file.
    The width and height are obtained based on the image file.
    """

    def __init__(self, image_file):
        super(GameImage, self).__init__()

        # Loads image from the source, converts to fast-blitting format
        self.image = pygame.image.load(image_file).convert_alpha()
        # Gets the image pygame.Rect
        self.rect = self.image.get_rect()

        # Size
        self.width = self.rect.width
        self.height = self.rect.height

    """Draws the image on the screen"""

    def draw(self):
        # A instance of the Window screen
        # Window object must've been instatiated
        # draw_rect is necessary to readjust the image position given .x and .y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Window.get_screen().blit(self.image, self.rect)

    """Sets the (X,Y) image position on the screen"""

    def set_position(self, x, y):
        self.x = x
        self.y = y

    """Checks collision with hitmask"""

    def collided_perfect(self, target):
        return Collision.collided_perfect(self, target)
