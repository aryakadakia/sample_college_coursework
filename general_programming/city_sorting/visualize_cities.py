from cs1lib import *

population_list = []
population_file = open("cities_population.txt", "r")

for line in population_file:
    line = line.strip()
    item = line.split(",")
    population_list.append(item)

population_file.close()

def draw_background():
    img = load_image("world.png")
    draw_image(img, 0, 0)

def draw_city(i, rad):
    if i >= 0:

        if float(population_list[i][3]) >= 0:
            long = float(population_list[i][3])*2 + 360
        if float(population_list[i][3]) < 0:
            long = 360 - abs(float(population_list[i][3]))*2
        lat = 180 - float(population_list[i][2])*2

        disable_stroke()
        set_fill_color(1,0,0)
        draw_circle(long, lat, rad)


first_time = True
index = 1

def draw_world_map():
    global first_time, index
    if first_time:
        draw_background()
        first_time = False

    if index <= 50:
        draw_city(index,3)
        index = index + 1


start_graphics(draw_world_map, width = 720, height = 360)