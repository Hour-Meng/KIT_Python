import turtle as t

SCORE = 0 # all cap as it's a global value

# Set up the screen
def screen_setup():
    window = t.Screen()

    # Customize the window
    window.title("Ping Pong Game")
    window.bgcolor(0.5,0.5,0.5) #bg color means background color, you can use both text(all small case) pr use hexadecimal color code(RGB)

    window.setup(width= 800, height = 600) #width and height of the window in pixels

    score = t.Turtle()
    score.hideturtle()
    score.penup()
    score.goto(-360, 260)
    score.write(f"Score: {SCORE}", font=("C059", 24, "normal"))


    ball = t.Turtle()
    ball.shape("circle")
    ball.shapesize(3,3)
    ball.color(0.4,0.3,0.7)


    plate = t.Turtle()
    plate.hideturtle()
    plate.penup()
    plate.setx(350)
    plate.shape("square")
    plate.shapesize(6,1)
    plate.showturtle()
    plate.pendown()

    move_value = 20

    def move_plate_up():

        if plate.ycor() > 220:
            print("Can't move anymore!")
            y = 220
            plate.sety(y)
        else:
            y = plate.ycor()
            print(y)
            y += move_value
            plate.sety(y)

    def move_palte_down():
        
        if plate.ycor() < -220:
            print("Can't move anymore!")
            y = -220
            plate.sety(y)
        else:
            y = plate.ycor()
            print(y)
            y -= move_value
            plate.sety(y)


    #map custom movement to keyboard
    window.listen()
    window.onkeypress(move_plate_up, "w")
    window.onkeypress(move_palte_down, "s")

    #ball logic to move



    
def main():
    screen_setup()



if __name__ == "__main__":
    main()


t.done()

