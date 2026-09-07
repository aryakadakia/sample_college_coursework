from cs1lib import *

rad = 5
w = 2


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj_list = []

    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, rad)
        enable_stroke()

    def draw_edge(self, vertex, r, g, b):
        set_stroke_color(r, g, b)
        set_stroke_width(w)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    def draw_all_edges(self, r, g, b):
        set_stroke_width(w)
        set_stroke_color(r, g, b)
        for i in range(len(self.adj_list)):
            draw_line(self.x, self.y, self.adj_list[i].x, self.adj_list[i].y)

    def boolean(self, x, y):
        return self.x - rad < x < self.x + rad and self.y - rad < y < self.y + rad

    def __str__(self):
        str_adj_list = ""
        for i in range(len(self.adj_list)-1):
            str_adj_list += self.adj_list[i].name + ", "

            str_adj_list += self.adj_list[len(self.adj_list)-1].name

        return str(self.name) + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + str(str_adj_list)
