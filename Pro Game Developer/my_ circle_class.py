import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)
Yellow  = (255, 255, 0)
screen.fill(White)

class mycircle():
    def __init__(self, color, pos, rad, wid = 0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn  = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)
    
    def grow(self, x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

position = (300, 300)
radius = 50
wid = 2
pygame.draw.circle(screen, Red, position, radius, wid)
pygame.display.update()

# Creating instances
Bluecircle = mycircle(Blue, position, radius + 60)
Redcircle = mycircle(Red, position, radius + 40)
Yellowcircle = mycircle(Yellow, position, radius, 5)
Greencircle = mycircle(Green, position, 20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            Bluecircle.draw()
            Redcircle.draw()
            Yellowcircle.draw()
            Greencircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            Bluecircle.grow(2)
            Redcircle.grow(2)
            Yellowcircle.grow(2)
            Greencircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = mycircle(Black, pos, 5)
            blackCircle.draw()
            pygame.display.update()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

    
#     pygame.display.update()