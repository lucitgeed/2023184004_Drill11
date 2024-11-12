from pico2d import load_image, clear_canvas, update_canvas, get_events
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDLK_SPACE, SDL_KEYDOWN

import game_framework


def init():
    global image
    image = load_image('images.png')

def finish():
    global image
    del image

def handle_events():  
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(800,300, 700,700)
    update_canvas()

def update(): pass

def pause(): pass
def resume():pass