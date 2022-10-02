# import colorgram
#
# extracted_colors = colorgram.extract("image", 30)
#
# color_list = []
# for color_object in extracted_colors:
#     color_rgb = color_object.rgb
#     color_tuple = color_rgb[0], color_rgb[1], color_rgb[2]
#     color_list.append(color_tuple)
#
# print(color_list)
import turtle
import random

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61),
              (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190),
              (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (166, 204, 202),
              (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33),
              (170, 203, 205), (223, 178, 169)]

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.setpos(-275, -250)
turtle.colormode(255)
t.speed("fastest")


def change_color():
    color_rgb = random.choice(color_list)
    color_r = color_rgb[0]
    color_g = color_rgb[1]
    color_b = color_rgb[2]
    t.color(color_r, color_g, color_b)


# 10x10 rows of spots

# Dots 20 in size and spaced 50 paces apart

for _ in range(10):
    for _ in range(10):
        t.forward(50)
        change_color()
        t.dot(20)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.left(180)

t.ht()

screen = turtle.Screen()
screen.exitonclick()
