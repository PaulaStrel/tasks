import turtle
turtle.speed(5)

turtle.shape('turtle')


def minkovsky (length, times):
    if times > 0:
        for deg in [90, -90, -90, 0, 90, 90, -90, 0]:
            minkovsky(length / 8, times - 1)
            turtle.left(deg)
    else:
        turtle.forward(length)


minkovsky(500,2)