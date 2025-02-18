import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
  pygame.init()
 # INITALIZES OBJECTS

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

 # GROUPS
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shot = pygame.sprite.Group()

 # CONTAINERS
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (updatable, drawable, shot)

 # ONLY SHOWN IN TERMINAL 
  print("Starting asteroids!", f"Screen width: {SCREEN_WIDTH}", f"Screen height: {SCREEN_HEIGHT}")
  #

  clock = pygame.time.Clock()
  dt = 0
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)
  asteroid_field = AsteroidField()


  while True:
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
         return  
     
     #limits framerate to 60 fps
     dt = clock.tick(60) / 1000
     # sets background
     screen.fill("black")
     updatable.update(dt)
     for asteroid in asteroids:
       if asteroid.collision(player):
         print("Game over!")
         sys.exit()
     for drawn in drawable:
       drawn.draw(screen)
     pygame.display.flip()


if __name__ == "__main__":
 main()