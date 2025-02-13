import pygame # type: ignore
from constants import *
from player import *
def main():
 pygame.init()

 screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

 print("Starting asteroids!", f"Screen width: {SCREEN_WIDTH}", f"Screen height: {SCREEN_HEIGHT}")
 clock = pygame.time.Clock()
 dt = 0
 x = SCREEN_WIDTH / 2
 y = SCREEN_HEIGHT / 2
 player = Player(x, y) 
 while True:
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
         return
     dt = clock.tick(60) / 1000
     screen.fill("black")
     player.draw(screen)
     pygame.display.flip()


if __name__ == "__main__":
 main()