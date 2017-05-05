import turtle

def draw_square() :
    window = turtle.Screen()
    # window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.speed(100)

    count = 0
    while count < 360 :
        brad.forward(1)
        brad.right(1)
        count = count + 1

    count = 0
    while count < 360 :
        brad.forward(1)
        brad.left(1)
        count = count + 1

    window.exitonclick()


draw_square()
