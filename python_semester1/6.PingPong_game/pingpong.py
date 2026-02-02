import turtle as t
import time

SCORE = 0 # all cap as it's a global value

# Set up the screen
def screen_setup(window: t.Screen):

    # Customize the window
    window.title("Ping Pong Game")
    window.bgcolor(0.5,0.5,0.5) #bg color means background color, you can use both text(all small case) pr use hexadecimal color code(RGB)

    window.setup(width= 800, height = 600) #width and height of the window in pixels

    score_display = t.Turtle()
    score_display.hideturtle()
    score_display.penup()

    width = window.window_width()/2 -40
    width = -width
    height = window.window_height()/2 -60

    score_display.goto(width, height)
    score_display.write(f"Score: {SCORE}", font=("C059", 24, "normal"))
    
    return score_display



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

    def move_palte_down():
        
        if plate.ycor() < -220:
            print("Can't move anymore!")
            y = -220
        else:
            plate.sety(plate.ycor()- move_value)

    #map custom movement to keyboard
    window.listen()
    window.onkeypress(move_plate_up, "w")
    window.onkeypress(move_palte_down, "s")
    
    return plate


def ball_physics(window: t.Screen, plate: t.Turtle, score_display: t.Turtle):
    # to turn off the automatic screen updates
    global SCORE
    
    ball = t.Turtle()
    ball.penup()
    ball.shape("circle")
    ball.shapesize(3,3)
    ball.color(0.4,0.3,0.7)
    ball.speed(0)  # disable built-in turtle animation delay

    ball.dy = 1.1  # to move the ball in y direction
    ball.dx = 1.1  # to move the ball in x direction
    
    last_hit_time = 0  # prevent multiple hits in quick succession

    #ball logic to move
    while True:
        #collision with top and bottom wall
        if ball.ycor() > window.window_height()/2 - 15 or ball.ycor() < -window.window_height()/2 + 15:
            ball.dy *= -1


        #collision with left and right wall
        if ball.xcor() > window.window_width()/2 - 15 or ball.xcor() < -window.window_width()/2 + 15:
            ball.dx *= -1

        
        # collision with plate - larger hitbox to match visual size
        current_time = time.time()
        if (ball.xcor() > plate.xcor() - 50 and ball.xcor() < plate.xcor() + 50 and
            ball.ycor() > plate.ycor() - 20 and ball.ycor() < plate.ycor() + 20 and
            current_time - last_hit_time > 0.2):  # 0.2 second cooldown
            
            ball.dx *= -1
            ball.setx(plate.xcor() - 55)  # push ball away from plate
            SCORE += 1
            last_hit_time = current_time
            
            # Update score display
            score_display.clear()
            score_display.write(f"Score: {SCORE}", font=("C059", 24, "normal"))
            print(f"Hit! Score: {SCORE}")

        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        window.update()
        time.sleep(1/240)  # steady frame rate


def main():
    window = t.Screen()
    window.tracer(0)  # to turn off the automatic screen updates
    score_display = screen_setup(window)
    plate = plate_logic(window)
    ball_physics(window, plate, score_display)





if __name__ == "__main__":
    main()


# custom control of output screen