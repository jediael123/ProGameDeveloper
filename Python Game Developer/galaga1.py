import pgzrun
import random

WIDTH  = 1200
HEIGHT = 600

ship = Actor("galaga")
bug = Actor("bug")

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 5

bullets = []
enemies = []

enemies.append(Actor("bug"))
enemies[-1].x = 10
enemies[-1].y = -100

score = 0
def displayScore():
    screen.draw.text(str(score), (50, 30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y -50

def update():
    global score
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0

    elif keyboard.right:
        ship.x += speed
        if ship.x >= 0:
            ship.x = WIDTH

    for bullet in bullets:
        #if the bullet reaches the top of the screen it should get removed
        #else the list will become huge
        if bullet.y <=0 :
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    
    for enemy in enemies:
        enemy.y += 5
        #as the bug touches the bottom, make it go back up
        if enemy.y >= HEIGHT:
            enemy.y  = -100
            enemy.x = random.randint(50,WIDTH-50)
        #checking if the enemy hits a bullet while moving down
        #iterate over all the bullets and check for a collision
        for bullet in bullets :
            if enemy.colliderect(bullet):
                score +=100
                #we also want to destory the bullet
                bullets.remove(bullet)
                #destroy the bug
                enemies.remove(enemy)

def draw():
    screen.clear()
    screen.fill("blue")
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    displayScore()

pgzrun.go()