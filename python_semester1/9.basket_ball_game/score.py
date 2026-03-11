import turtle as t

class Score(t.Turtle):

    main_score = 0
    def __init__(self, x_cor:int|float, y_cor:int|float):
        self.x_cor = x_cor
        self.y_cor = y_cor
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(f"Score: {self.main_score}/10", font=("Arial", 20, "bold"))


    def update_score(self):
        self.main_score += 1
        self.clear()
        self.write(f"Score: {self.main_score}/10", font=("Arial", 20, "bold"))

