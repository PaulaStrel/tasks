import turtle

turtle.shape('turtle')


def koch (length, times):
    if times > 0:
        for deg in [60, -120, 60, 0]:
            koch(length / 3, times - 1)
            turtle.left(deg)
    else:
        turtle.forward(length)


koch(500, 3)