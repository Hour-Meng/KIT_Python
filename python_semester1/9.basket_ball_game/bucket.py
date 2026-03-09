import turtle as t

class Bucket(t.Turtle):
    def __init__(self, image_asset: str, y_cor: int| float):
        self.asset = image_asset
        self.y_cor = y_cor
        super().__init__()
        self.penup()
        self.shape(image_asset)
        self.goto(0, y_cor)

    def move_left(self):
        if self.xcor() > -280:
            self.setx(self.xcor() - 20)
        else:
            self.setx(-280)

    def move_right(self):
        if self.xcor() < 280:
            self.setx(self.xcor() + 20)
        else:
            self.setx(280)
        