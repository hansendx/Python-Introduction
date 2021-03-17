import turtle

from math import pi, sqrt
from typing import Tuple

turtle.reset()

SIZE_MODIFIER: int = 4
CIRCLE_DETAIL = 200


def point_distance(point_x, point_y) -> float:
    return sqrt(((point_x[0] - point_y[0]) ** 2) + (point_x[1] - point_y[1]) ** 2)


def circumference(radius: float) -> float:
    return 2 * pi * radius


def draw_wind_rose():
    points = 8
    inside_angle = 360 / points
    left_most_point: Tuple[float, float] = (0.0, 0.0)
    right_most_point: Tuple[float, float] = (0.0, 0.0)
    outer_points = list()
    for line in range(points + 1):
        turtle.forward(100 * SIZE_MODIFIER)
        if line % 2 == 0:
            turtle.left(inside_angle * 3 + 15)
            outer_points.append(turtle.pos())
        else:
            turtle.left(inside_angle * 3 - 15)

    radius = point_distance(outer_points[0], outer_points[2]) / 2
    return {"radius": radius, "inside_angle": inside_angle}


def draw_circle(circumference: float):
    for _ in range(CIRCLE_DETAIL):
        turtle.left(360 / CIRCLE_DETAIL)
        turtle.forward(circumference / CIRCLE_DETAIL)


if __name__ == "__main__":
    turtle.left(16)
    star_detail = draw_wind_rose()
    turtle.width(turtle.width() + 3)
    turtle.colormode(255)
    turtle.color(240, 100, 100)
    turtle.right(90 - (star_detail["inside_angle"] - 15) / 2)
    circle_circumference = circumference(radius=star_detail["radius"])
    draw_circle(circle_circumference)
    turtle.done()
