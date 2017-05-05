import turtle

def draw_square() :
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.speed(100)

    count = 0
    while count < 4 :
        brad.forward(100)
        brad.right(90)
        count = count + 1


def draw_circle() :
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("white")
    brad.speed(100)

    brad.left(120)
    brad.forward(100)
    brad.color("black")
    brad.circle(50)


def draw_triangle() :
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("white")
    brad.speed(100)

    brad.left(120)
    brad.forward(200)
    brad.color("black")

    count = 0
    while count < 3 :
        brad.forward(100)
        brad.right(120)
        count = count + 1


window = turtle.Screen()
    
draw_square()
draw_circle()
draw_triangle()
        
window.exitonclick()
