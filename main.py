import turtle as t

tim = t.Turtle()
screen = t.Screen()
tim.up()

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def draw_toggle():
    if tim.isdown():
        tim.up()
    else:
        tim.down()


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def screen_clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(draw_toggle, "space")
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(screen_clear, "c")
screen.exitonclick()