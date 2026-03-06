import turtle as t
import time, random

window = t.Screen()
window.setup(800,600)
window.bgcolor("#76737e")
t.tracer(0)

#score
class Score(t.Turtle):
    def __init__(self, score:int, x_cor:int|float , y_cor:int|float):
        self.score = score
        self.x_cor = x_cor
        self.y_cor = y_cor
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_cor, y_cor)
        self.write(f"Score: {score}" ,font=("Arial", 20, 'bold'))

main_score_A , main_score_B = 0, 0
score_A = Score(main_score_A, -380, 270)
score_B = Score(main_score_B, 270, 270)

#ball
ball = t.Turtle()
ball.penup()
ball.shape("circle")
ball.shapesize(2,2)
ball.dx = 4
ball.dy = 4



# Main class of turtle
class Paddle(t.Turtle):
    def __init__(self, x_cor: int|float, color: str):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(6,1)
        self.color(color)
        self.goto(x_cor, 0)

    def go_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)
        else:
            self.sety(250)

    def go_down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 20)
        else:
            self.sety(-250)


paddle_A = Paddle(-385, "red")
paddle_B = Paddle(380, "black")

window.listen()
# for A
window.onkeypress(paddle_A.go_up, "a")
window.onkeypress(paddle_A.go_down, "d")
# for B
window.onkeypress(paddle_B.go_up, "j")
window.onkeypress(paddle_B.go_down, "l")
FPS = 240

#AI config
ai_move_speed = 10
ai_delay_time = random.randint(10, 50)


while main_score_A < 10 and main_score_B < 10:
    # AI behavior
    if paddle_B.distance(ball) < 300:
        if ball.ycor() > paddle_B.ycor():
            paddle_B.sety( paddle_B.ycor() + ai_move_speed )
        elif ball.ycor() < paddle_B.ycor():
            paddle_B.sety( paddle_B.ycor() - ai_move_speed)
    if paddle_A.distance(ball) < 300:
        if ball.ycor() > paddle_A.ycor():
            paddle_A.sety(paddle_A.ycor() + ai_move_speed )
        elif ball.ycor() < paddle_A.ycor():
            paddle_A.sety( paddle_A.ycor() - ai_move_speed )

    # make sure the ball stay in bound
    if ball.xcor() < -400 or ball.xcor() > 400: 
        ball.dx *= -1
        if ball.xcor() < -400:
            main_score_B += 1
            score_B.clear()
            score_B.write(f"Score: {main_score_B}" ,font=("Arial", 20, 'bold'))
            print("Hit A")
        else:
            main_score_A += 1
            score_A.clear()
            score_A.write(f"Score: {main_score_A}" ,font=("Arial", 20, 'bold'))


    
    if ball.ycor() < -300 or ball.ycor() > 300:
        ball.dy *= -1

    if ball.distance(paddle_A) < 20 or ball.distance(paddle_B) < 20:
        ball.dx *= -1

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # to make the frame steady
    time.sleep(1/FPS)
    window.update()
#winner screan
winner = t.Turtle()
winner.hideturtle()
winner.penup()
if main_score_A > main_score_B:
    winner.write("Player A won" , font=("Arial", 20, "bold"), align="center")
else:
    winner.write("Player B won" , font=("Arial", 20, "bold"), align="center")
t.done()
