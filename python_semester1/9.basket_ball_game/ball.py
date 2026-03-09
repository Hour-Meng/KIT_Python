import turtle as t
import os
import random
s_dir = os.path.dirname(os.path.abspath(__file__))
ball_file = os.path.join(s_dir, "bk_ball_r_d.gif")


class Ball(t.Turtle):
    possible_y = (280, 320, 360, 390)
    def __init__(self, ball_file):

        super().__init__()
        self.penup()
        self.shape(ball_file)
        
        self.random_x = random.randint(-280, 280)
        self.random_y = random.choice(self.possible_y) # choice needed to be an array, and it will only choose 1
        self.goto(self.random_x, self.random_y)
        # The speed of it
        self.dy = random.uniform(2, 4) # this will increase the value in a curve type

    def move_down(self):
        self.sety(self.ycor() - self.dy)

        if self.ycor() < -400:
            self.despawn()

    def despawn(self):
        self.random_x = random.randint(-280, 280)
        self.random_y = random.choice(self.possible_y) 
        self.goto(self.random_x, self.random_y)
        
