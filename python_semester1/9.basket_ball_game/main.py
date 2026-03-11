import turtle as t
import os, time
from bucket import Bucket
from ball import Ball
from score import Score

# Get absolute paths from this file's folder so run location does not matter.
script_dir = os.path.dirname(os.path.abspath(__file__))
basket_ball_bg = os.path.join(script_dir, "basketball_bg.gif")
ball_object = os.path.join(script_dir, "bk_ball_r_d.gif")
bk_hoop = os.path.join(script_dir, "bk_h_r_d.gif")
coin_sound = os.path.join(script_dir, "coin_sound.mp3") # currently will not work, I haven't found a way to play sound in python without using a module, and I don't want to use any modules for this project. So I will just leave it here for now, maybe I will find a way to play it later on.


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

# ===================================================================================================================== #

                                                            # game setting
#Score = 0

"""score = t.Turtle()
score.hideturtle()
score.penup()
score.goto( -280 , 360)
score.write(f"Score: {Score}/10", font=("Arial", 20, "bold"))

def update_score():
    global Score
    Score += 1
    score.clear()
    score.write(f"Score: {Score}/10", font=("Arial", 20, "bold"))"""

score_board = Score(-280 , 360)
    
FPS = 60
AI = True # My AI is still bad, I will config it once I have enough knowledge of it
AI_movement = 20

# ===================================================================================================================== #

                                                            # Main Game

while score_board.main_score < 10:
    window.update()
    # this here will update the ball

    for ball in ball_ls:
        # AI Play
        if AI:
            if ball.xcor() < main_hoop.xcor():
                main_hoop.setx(main_hoop.xcor() - AI_movement)
            elif ball.xcor() > main_hoop.xcor():
                main_hoop.setx(main_hoop.xcor() + AI_movement)
            elif main_hoop.xcor() == ball.xcor():
                main_hoop.setx(main_hoop.xcor())
                 
        # touch function
        if main_hoop.distance(ball) < 30:
            ball.respawn()
            score_board.update_score()
            
        ball.move_down() # call it's function


    time.sleep(1/FPS)

# ===================================================================================================================== #

                                                            # Display Winning Screen

win = t.Turtle()
win.color("#1f2223")
win.write("You Win the Game", font=("Arial", 40, "bold"), align= "center")
t.done()