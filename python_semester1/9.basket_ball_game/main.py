import turtle as t
import os, time
from bucket import Bucket
from ball import Ball

# Get absolute paths from this file's folder so run location does not matter.
script_dir = os.path.dirname(os.path.abspath(__file__))
basket_ball_bg = os.path.join(script_dir, "basketball_bg.gif")
ball_object = os.path.join(script_dir, "bk_ball_r_d.gif")
bk_hoop = os.path.join(script_dir, "bk_h_r_d.gif")

# ===================================================================================================================== #
                                                            # Main Window
window = t.Screen()
window.setup(600, 800)
window.title("Basket Ball Game")
window.tracer(0)
# give it the background
window.bgpic(basket_ball_bg)

# ===================================================================================================================== #

                                                            # the hoop
window.addshape(bk_hoop)
main_hoop = Bucket(bk_hoop, -360)

window.listen()
window.onkeypress(main_hoop.move_left, "a")
window.onkeypress(main_hoop.move_right, "d")

# ===================================================================================================================== #

                                                            # the ball
window.addshape(ball_object)
ball_ls =  list()
for _ in range(5):
    g_ball = Ball(ball_object)
    ball_ls.append(g_ball)

print(ball_ls)

# ===================================================================================================================== #

                                                            # game setting
Score = 0

score = t.Turtle()
score.hideturtle()
score.penup()
score.goto( -280 , 360)
score.write(f"Score: {Score}/10", font=("Arial", 20, "bold"))

FPS = 60

# ===================================================================================================================== #

                                                            # Main Game

while Score < 10:
    window.update()
    # this here will update the ball

    for ball in ball_ls:
        # AI Play
        if main_hoop.distance(ball) < 50:
            main_hoop.setx(ball.xcor())

        # touch function
        if main_hoop.distance(ball) < 30:
            ball.despawn()
            Score += 1
            score.clear()
            score.write(f"Score: {Score}/10", font=("Arial", 20, "bold"))
        ball.move_down() # call it's function


    time.sleep(1/FPS)

# ===================================================================================================================== #

                                                            # Display Winning Screen

win = t.Turtle()
win.color("#1f2223")
win.write("You Win the Game", font=("Arial", 40, "bold"), align= "center")
t.done()