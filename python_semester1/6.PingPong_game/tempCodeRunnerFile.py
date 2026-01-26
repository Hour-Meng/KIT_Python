import turtle as t
import time

SCORE = 0 # all cap as it's a global value

# Set up the screen
def screen_setup(window: t.Screen):

    # Customize the window
    window.title("Ping Pong Game")
    window.bgcolor(0.5,0.5,0.5) #bg color means background color, you can use both text(all small case) pr use hexadecimal color code(RGB)

    window.setup(width= 800, height = 600) #width and height of the window in pixels

    score = t.Turtle()
    score.hideturtle()
    score.penup()

    width = window.window_width()/2 -40
    width = -width
    height = window.window_height()/2 -60

    score.goto(width, height)
    score.write(f"Score: {SCORE}", font=("C059", 24, "normal"))



def plate_logic(window: t.Screen):

    plate = t.Turtle()
    plate.hideturtle()
    plate.penup()
    plate.setx(window.window_width()/2-20)
    plate.shape("square")
    plate.shapesize(6,1)
    plate.showturtle()
    

    move_value = 20

    def move_plate_up():

        if plate.ycor() > 220:
            print("Can't move anymore!")
            y = 220

        else:
 
            plate.sety(plate.ycor()+ move_value)
        
        print(f"{plate.position()}")
            

    def move_palte_down():
        
        if plate.ycor() < -220:
            print("Can't move anymore!")
            y = -220
        else:
            plate.sety(plate.ycor()- move_value)
        
        
        print(f"{plate.position()}")


    #map custom movement to keyboard
    window.listen()
    window.onkeypress(move_plate_up, "w")
    window.onkeypress(move_palte_down, "s")


def ball_physics(window: t.Screen):
    # to turn off the automatic screen updates
    ball = t.Turtle()
    ball.penup()
    ball.shape("circle")
    ball.shapesize(3,3)
    ball.color(0.4,0.3,0.7)
    ball.speed(0)  # disable built-in turtle animation delay

    ball.dy = 1.1  # to move the ball in y direction
    ball.dx = 1.1  # to move the ball in x direction

    #ball logic to move
    while True:
        global SCORE
        #collision with top and bottom wall
        if ball.ycor() > window.window_height()/2 - 15 or ball.ycor() < -window.window_height()/2 + 15:
            ball.dy *= -1
            print(f"Bounce! Y wall {ball.dx}, {ball.dy}")

            SCORE += 1

        #collision with left and right wall
        if ball.xcor() > window.window_width()/2 - 15 or ball.xcor() < -window.window_width()/2 + 15:
            ball.dx *= -1
            print(f"Bounce! X wall {ball.dx}, {ball.dy}")

            SCORE += 1

        

        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        window.update()
        time.sleep(1/240)  # steady frame rate
        print(SCORE)

def score_update(window: t.Screen):
    ball = ball_physics(window)
    plate = plate_logic(window)

    if ball < plate + 10 and ball > plate -10:
        global SCORE
        SCORE += 1
        print(f"Score: {SCORE}")
    
def main():
    window = t.Screen()
    window.tracer(0)  # to turn off the automatic screen updates
    screen_setup(window)
    plate_logic(window)
    ball_physics(window)





if __name__ == "__main__":
    main()
