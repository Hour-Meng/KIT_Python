import turtle

# Debugging the maze escape

def maze_escape():

    turtle.forward(100)

    turtle.left(90)

    turtle.forward(100)

    turtle.right(90)

    turtle.forward(100)

    turtle.left(90) # this one was turning right (turn it to turning left)

    turtle.forward(100)

# Debugging: Incorrect angle for turning

turtle.speed(1) # Set turtle speed

maze_escape()

turtle.done()