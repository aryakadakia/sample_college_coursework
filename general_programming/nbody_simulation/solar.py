from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 7e6
PIXELS_PER_METER = 9 / 1e10

FRAMERATE = 30
TIMESTEP = 1.0 / FRAMERATE

def main():
    set_clear_color(0, 0, 0)

    clear()

    solar_system.draw(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, PIXELS_PER_METER)

    solar_system.update(TIME_SCALE*TIMESTEP)


sun = Body(1.98892e30, 0, 0, 0, 0, 30, 1, 1, 0)
mercury = Body(0.330e24, 57.9e9, 0, 0, 47.4e3, 5, 0, 1, 1)
venus = Body(4.87e24, 108.2e9, 0, 0, 35e3, 7, 1, 0.5, 0)
earth = Body(5.97e24, 149.6e9, 0, 0, 29.8e3, 8, 0, 0, 1)
mars = Body(0.642e24, 227.9e9, 0, 0, 24.1e3, 6, 1, 0, 0)
jupiter = Body(1898e24, 778.6e9, 0, 0, -13.1e3, 20, 1, 0.5, 0)
saturn = Body(568e24, 1433.5e9, 0, 0, -9.7e3, 15, 0.9, 0.5, 0.4)
uranus = Body(86.8e24, 2872.5e9, 0, 0, -6.8e3, 9, 0, 0, 1)
neptune = Body(102e24, 4495.1e9, 0, 0, -5.4e3, 10, 0, 0.3, 1)

solar_system = System([sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune])

start_graphics(main,2400,framerate=FRAMERATE)