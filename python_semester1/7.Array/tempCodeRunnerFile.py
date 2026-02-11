import turtle as t
import random
score = 20
#Window setup
window = t.Screen()
window.setup(width = 600, height = 800)
window.bgcolor("#514553")
#Score board
window.title("Fruit Game")
score_board = t.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-80, 350)
score_board.write(f"Score: {score}", font= ("Michroma", 25, 'bold'))
score_board.pendown()
#bucket
bucket = t.Turtle()
bucket.hideturtle()
bucket.shape("triangle")
bucket.setheading(270)
bucket.shapesize(2, 3)
bucket.penup()
bucket.goto(0,-250)
bucket.showturtle()
bucket.pendown()
#moving logic for bucket
def move_left(): # we move left using "A" key
    move = 20
    if bucket.xcor() < (window.window_width()/2)*-1 + 30:
        bucket.setx(bucket.xcor())
        print("Can't move anymore!")
    else:
        bucket.setx(bucket.xcor() - move)
def move_right(): # we move right using "D" key 
    move = 20
    if bucket.xcor() > (window.window_width()/2) -30:
        bucket.setx(bucket.xcor())
    else:
        bucket.setx(bucket.xcor() + move)
# The moving logic
window.listen()
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
# our fruits
def create_fruit():
    fruit = t.Turtle()
    fruit.hideturtle()
    fruit.shape("circle")
    fruit.penup()
    fruit.color(random.choice(["red", "blue", "green", "pink", "brown"]))
    fruit.setposition(random.randint(-280, 280), random.randint(300, 380))
    fruit.shapesize(2,2)
    fruit.showturtle()
    return fruit
fruits = []
for i in range(5):
    fruits.append(create_fruit())
print(fruits)

t.done()