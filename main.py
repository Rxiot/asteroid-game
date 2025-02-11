import pygame
from constants import *
def main():
 pygame.init()

 screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

 print("Starting asteroids!", f"Screen width: {SCREEN_WIDTH}", f"Screen height: {SCREEN_HEIGHT}")
 while True:
     screen.fill("black")
     pygame.display.flip()


if __name__ == "__main__":
 main()