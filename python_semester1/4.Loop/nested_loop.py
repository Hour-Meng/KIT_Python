# Nested loop is a kind of loop that is in a loop

"""for i in range (0,2):
    print(i)
    print()
    for i in range(0,5):
        print(f"{i+1} New line")
"""

import turtle as t

sqaure_draw = t.Turtle()
sqaure_draw.hideturtle()


sqaure_draw.penup()
sqaure_draw.goto(-200,0)
sqaure_draw.pendown()

for _ in range(3):  
          
    sqaure_draw.begin_fill()
    sqaure_draw.fillcolor("red")

    for _ in range(4):

        sqaure_draw.forward(100)
        sqaure_draw.left(90)

    sqaure_draw.end_fill()

    sqaure_draw.penup()
    sqaure_draw.forward(120)
    sqaure_draw.pendown() # This will draw 3 red squares
t.done()

