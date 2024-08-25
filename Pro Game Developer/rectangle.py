import pygame
pygame.init()

# Set dimensions of the screen
screen = pygame.display.set_mode((600, 600))

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(white)
pygame.display.update()

# Create a rectangle class
class Rect():
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

# Creating instances
greenrect = Rect(green, (50, 20, 130, 70))
redrect = Rect(red, (150, 200, 155, 95))
bluerect = Rect(blue, (300, 300, 65, 187 ))

# Accessing methods
greenrect.draw()
bluerect.draw()
redrect.draw()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()



pygame.display.update()
