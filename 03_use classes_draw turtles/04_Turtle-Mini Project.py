import turtle

def draw_star(some_turtle, distance) :
    for i in range(1, 6) :
        some_turtle.forward(distance)
        some_turtle.right(145)

window = turtle.Screen()
brad = turtle.Turtle()
brad.shape("arrow")
brad.color("black")
brad.speed(100)

draw_star(brad, 100)
        
window.exitonclick()
