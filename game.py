import pygame, sys
from pygame.locals import *

pygame.init()

while True: #the game loop
  #Handle Events
  for event in pygame.event.get():
    #Update Game State
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  #Draw The Screen
  pygame.display.update()