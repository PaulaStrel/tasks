import turtle

turtle.shape('turtle')


def koch (length, times):
    if times > 0:
        for deg in [60, -120, 60, 0]:
            koch(length / 3, times - 1)
            turtle.left(deg)
    else:
        turtle.forward(length)

for i in range(3):
    koch(500, 3)
    turtle.right(120)