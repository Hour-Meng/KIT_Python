import turtle as t
window = t.Screen()
window.bgcolor("black")
hexa_gon = t.Turtle()
hexa_gon.speed(10000)
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

i = 0

while i < 400:
    hexa_gon.color(color_list[i % 6])
    hexa_gon.pensize(i/100 + 1)
    hexa_gon.forward(i)
    hexa_gon.right(60)
    i+= 1
t.done()