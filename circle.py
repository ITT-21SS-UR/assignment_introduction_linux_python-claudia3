import turtle
import sys
import math
import random


__INVALID_INPUT = "There is no radius...\n" \
                  "So the little turtle 🐢 can't draw a circle ⭕\n" \
                  "Little turtle is very sad 😭\n"


def exit_program():
    sys.stderr.write(__INVALID_INPUT)
    sys.exit(1)


def get_radius():
    if len(sys.argv) == 2:
        try:
            return abs(int(sys.argv[1]))
        except ValueError:
            exit_program()
    else:
        exit_program()


def move_to_start_position(start_position: tuple):
    turtl.penup()
    turtl.hideturtle()

    turtl.setposition(start_position)

    turtl.pendown()
    turtl.showturtle()


def move_turtle(radius: int):
    turtl.begin_fill()

    # b = r·π·α / 180°
    degrees = 360  # a full circle has 360°
    while degrees > 0:
        turtl.right(1)  # rotate the turtle with 1°
        turtl.forward(radius * math.pi / 180)
        degrees -= 1

    turtl.end_fill()


def setup_turtle():
    turtl.color("green")
    turtl.speed(100)


def draw_circle():
    radius = get_radius()

    move_to_start_position(turtle.Vec2D(0, radius))
    move_turtle(radius)

    turtle.done()


if __name__ == "__main__":
    turtl = turtle.Turtle(shape="turtle")
    setup_turtle()
    draw_circle()
