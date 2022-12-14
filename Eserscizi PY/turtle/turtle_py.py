import turtle


def main():
    dima = turtle.Turtle()
    finesta = turtle.Screen()
    dima.penup()
    dima.setposition(-30,-30)
    dima.pendown()
    dima.color("green")
    dima.speed(0)
    for _ in range(0,3600):
        dima.forward(0.1)
        dima.right(0.1)

    turtle.done()


if __name__ == "__main__":
    main()