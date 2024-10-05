import pygame
from time import *
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([600, 600])
Player_x = 200
Player_y = 200
keys = [False, False, False, False]
Player = pygame.image.load("Character.png")
Backround = pygame.image.load("Background.png")

while Player_y < 600:
    screen.blit(Backround, (0, 0))
    screen.blit(Player, (Player_x, Player_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


        #check if any keyboard button is pressed
        if event.type == pygame.KEYDOWN:
            #check which button is pressed
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        
        #check if any keyboard button is released
        if event.type == pygame.KEYUP:
            #check which button is released
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_LEFT:
                keys[1]=False
            elif event.key==K_DOWN:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False

    # If the up button is pressed
    if keys [0]: 
         if Player_y> 0:     # If the coordinate is greater than 0 (not outside the playing field)
             Player_y -= 7 # Change the y position by  pixels. The player moves upwards
    # If the down key is pressed
    elif keys [2]: 
         if Player_y <536: # If the coordinate is less than the height of the playing field
             Player_y += 7     # Change the y position by 2 pixels. The player goes down
    # Update x-position
    # If the left key is pressed
    if keys [1]: 
         if Player_x> 0:      # If the player is inside the playing field
             Player_x -= 2  # Decrease x position. The player goes left
    # If the right key is pressed
    elif keys [3]: 
         if Player_x <536: # If the player is inside the playing field
             Player_x += 2    # Increase x position. The player goes right
       
      #Update the rocket's vertical position using its current speed
    Player_y += 5
    sleep(0.05)

print("Game Over")