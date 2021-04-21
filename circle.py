import math
import sys
import turtle

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


def setup_turtle():
    turtle.Screen().bgcolor("#caede0")
    turtl.color("#77f99e")
    turtl.pencolor("black")
    turtl.pensize(2)
    turtl.speed("fast")


def move_to_position(position: tuple):
    turtl.penup()
    turtl.hideturtle()

    turtl.setposition(position)

    turtl.pendown()
    turtl.showturtle()


def draw_circle():
    move_to_position(turtle.Vec2D(0, radius))
    turtl.begin_fill()

    # b = r·π·α / 180°
    degrees = 360  # a full circle has 360°
    while degrees > 0:
        turtl.right(1)
        turtl.forward(radius * math.pi / 180)
        degrees -= 1

    turtl.end_fill()


def draw_star():
    move_to_position(turtle.Vec2D(0, radius))
    turtl.fillcolor("black")
    turtl.begin_fill()

    turtl.right(72)
    for i in range(5):
        turtl.forward(radius * 1.893)  # only approximately
        turtl.right(144)

    turtl.end_fill()


if __name__ == "__main__":
    radius = get_radius()

    turtl = turtle.Turtle(shape="turtle")
    setup_turtle()

    draw_circle()
    draw_star()

    turtl.hideturtle()
    turtle.done()
