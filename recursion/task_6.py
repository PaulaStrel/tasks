import turtle

turtle.shape('turtle')
turtle.speed(1)


def levi(length, times):
    if times > 0:
        for deg in [-90, 90]:
            levi(length / 2, times - 1)
            turtle.left(deg)
    else:
        turtle.forward(length)

levi(300, 4)