import turtle as t

spiral = t.Turtle()
color_list = ["red", "blue", "green", "yellow", "purple", "orange"]
window = t.Screen()
window.bgcolor("black")

for i in range(100):
    max_range = i % len(color_list)
    spiral.right(20)
    spiral.color(color_list[(max_range)])
    spiral.forward(i)
    

t.done()