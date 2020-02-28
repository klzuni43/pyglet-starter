import pyglet
win = pyglet.window.Window()
# load the image y create the sprite 
img = pyglet.image.load('assets/hero/sliced/idle-1.png')
spr = pyglet.sprite(img, x = 300, y = 200)

def update(dt):
    pass

@win.event
def on_draw():
    win.clear()
    # draw the sprite 
    spr.draw()

pyglet.clock.schedule(update)
pyglet.app.run()

import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/forest-assets/door.png')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(img, (400, 300))


    pygame.display.update()

pygame.quit()