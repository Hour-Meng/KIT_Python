import turtle as t

window = t.Screen()
window.setup(800,600)
window.bgcolor("#76737e")
t.tracer(0)

class Paddle:
    # basic and shape of it (the data)
    def __init__(self, p_color: str, x_cor: int| float):
        self.paddle = t.Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.shapesize(6, 1)
        self.paddle.color(p_color)
        self.paddle.goto(x_cor, 0)
    
    # the function part ( what it can do)

    def go_up(self):
        if self.paddle.ycor() < 250:
            self.paddle.sety(self.paddle.ycor() + 20)
        else:
            self.paddle.sety(250)

    def go_down(self):
        if self.paddle.ycor() > -250:
            self.paddle.sety(self.paddle.ycor() - 20)
        else:
            self.paddle.sety(-250)

# invoke the class
 
paddleA = Paddle("red", -385)
paddleB = Paddle("blue", 380)

window.listen()
# for paddle A
window.onkeypress(paddleA.go_up, "a")
window.onkeypress(paddleA.go_down, "d" )
# for Paddle B
window.onkeypress(paddleB.go_up, "Up")
window.onkeypress(paddleB.go_down, "Down" )

# since we 
while True:
    window.update()
 

