import turtle as t
import os
from bucket import Bucket

# Get the directory of this script, then find diddy.png in that directory
script_dir = os.path.dirname(os.path.abspath(__file__))
basket_ball_bg = os.path.join(script_dir, "basketball_bg.gif") # Replace with your image file name
ball_object = os.path.join(script_dir, "ball.gif") # Replace with your image file name
shopping_cart = os.path.join(script_dir, "shopping_cart.gif")

# ===================================================================================================================== #

window = t.Screen()
window.setup(600, 800)
window.title("Basket Ball Game")
window.tracer(0)

# give it the background
window.bgpic(basket_ball_bg)
# the ball
window.addshape("shopping_cart.gif")
game_bucket = Bucket("shopping_cart.gif", -350)

while True:
    window.update()