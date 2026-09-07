from vertex import *
from load_graph import *
from bfs import *

vert_dictionary = load_graph("dartmouth_graph.txt")
start = None
goal = None
load = True


def draw_background():
    map = load_image("dartmouth_map.png")
    draw_image(map, 0, 0)


def draw_vertices_edges():
    for vertex in vert_dictionary:
        vert_dictionary[vertex].draw_vertex(0, 0, 1)
        vert_dictionary[vertex].draw_all_edges(0, 0, 1)


def press(x, y):
    global start, goal
    for vertex in vert_dictionary:
        if vert_dictionary[vertex].boolean(x, y):
            start = vert_dictionary[vertex]
            start.draw_vertex(1, 0, 0)


def move(x, y):
    global goal
    for v in vert_dictionary:
        if start is not None and (vert_dictionary[v].boolean(x, y)):
            goal = vert_dictionary[v]


def draw_path(start, goal):
    path = bfs(start, goal)
    for i in range(len(path) - 1):
        path[i].draw_vertex(1, 0, 0)
        path[i].draw_edge(path[i + 1], 1, 0, 0)


def draw_all():
    global load
    if load:
        draw_background()
        load = False
    draw_vertices_edges()
    if start is not None:
        start.draw_vertex(1, 0, 0)
    if start is not None and goal is not None:
        draw_path(start, goal)


start_graphics(draw_all, mouse_move=move, mouse_press=press, width=1012, height=811)
