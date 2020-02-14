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

