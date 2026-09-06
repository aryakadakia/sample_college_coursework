from math import *

G = 6.67384 * (1/(10**11))


class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx,cy,pixels_per_meter)

    def compute_acceleration(self, n):
        total_ax = 0
        total_ay = 0

        for i in range(len(self.body_list)):
            if i != n:
                dx = self.body_list[i].x - self.body_list[n].x
                dy = self.body_list[i].y - self.body_list[n].y
                r = sqrt((dx**2) + (dy**2))
                a = (G * self.body_list[i].mass)/(r**2)
                ax = a * (dx/r)
                ay = a * (dy/r)
                total_ax = total_ax + ax
                total_ay = total_ay + ay
        return total_ax, total_ay

    def update(self, timestep):
        for n in range(len(self.body_list)):
            self.body_list[n].update_position(timestep)
            total_ax, total_ay = self.compute_acceleration(n)
            self.body_list[n].update_velocity(total_ax, total_ay, timestep)


