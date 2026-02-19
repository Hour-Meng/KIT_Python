import turtle as t
import random
import time
score = 0
FPS = 60
#Window setup
window = t.Screen()
window.setup(width = 600, height = 800)
window.bgcolor("#514553")
window.tracer(1) # to make the game run smoother
#Score board
window.title("Fruit Game")
score_board = t.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-100, 350)
score_board.write(f"Score: {score}", font= ("Michroma", 25, 'bold'))
score_board.pendown()
#bucket
bucket = t.Turtle()
bucket.hideturtle()
bucket.shape("triangle")
bucket.setheading(270)
bucket.shapesize(3, 4)
bucket.penup()
bucket.goto(0,-250)
bucket.showturtle()

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
# our fruits
fruits = []
def create_fruit():
    fruit = t.Turtle()
    fruit.penup()
    fruit.hideturtle()
    fruit.goto(random.randint(-280, 280), random.randint(300, 380))
    fruit.shape("circle")
    fruit.color(random(fruits_dic.values()))
    
    fruit.shapesize(2,2)
    fruit.showturtle()
    fruits.append(fruit)

def floating_points(caught_fruit):
    point = t.Turtle()
    point.hideturtle()
    point.penup()
    point.goto(caught_fruit.xcor(), caught_fruit.ycor())
    point.write("+1", font= ("Michroma", 15, 'bold'))
    float_point_list.append(point)

#dictionary of fruits
fruits_dic  = {"apple":"#fb542b", 
               "banana":"#edfb2b",
                 "grape":"#b12bfb", 
                 "strawberry":"#d96565",
                   "coconut":"#fcf8f8"}

float_point_list = list() # to store the floating points


wining_score = 20
#fruit falling logic
while score < wining_score:
    # The moving logic
    window.listen()
    window.onkeypress(move_left, "a")
    window.onkeypress(move_right, "d")
    window.tracer(0) # to make the game run smoother
    # spawn the fruit
    for fruit in fruits_dic:
        fruit.sety(fruit.ycor() - 5)
        # when fruit touched the ground
        if fruit.ycor() < -300:
            fruit.hideturtle()
            fruits_dic.remove(fruit)

        # when fruit touched the bucket
        if bucket.distance(fruit) < 10:
            score_board.clear()
            score += 1
            score_board.write(f"Score: {score}", font= ("Michroma", 25, 'bold'))
            fruit.hideturtle()
            fruits_dic.remove(fruit)
  


    time.sleep(1/FPS) # to give a steady frame rate
    window.update()
    window.tracer(1)

win_screen = t.Turtle()
win_screen.hideturtle()
win_screen.penup()
win_screen.write("Congratulations!!", font=("Arial", 30, "bool"))
t.done()