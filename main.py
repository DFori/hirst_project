import random
import colorgram
import turtle as t
tim = t.Turtle()
t.colormode(255)
rgb_colors = [
(28, 109, 184),
(225, 61, 90),
(224, 151, 90),
(124, 153, 205),
(215, 130, 162),
(139, 89, 52),
(38, 194, 107),
(105, 108, 190),
(140, 177, 27),
(240, 155, 184),
(186, 48, 80),
(109, 192, 156),
(224, 63, 55),
(186, 18, 37),
(20, 182, 210),
(146, 221, 172),
(39, 53, 115),
(136, 217, 230),
(239, 172, 157),
(176, 174, 227),
(25, 149, 113),
(36, 36, 69),
(187, 218, 9),
(76, 28, 33),
(75, 35, 29)]
def draw_line():
    x = -250
    y = -200
    for i in range(10):
        tim.penup()
        tim.setposition(x, y)
        y += 40
        for j in range(11):
            tim.color(random.choice(rgb_colors))
            tim.width(12)
            tim.forward(1)
            tim.penup()
            tim.forward(40)
            tim.pendown()
draw_line()

screen = t.Screen()
screen.exitonclick()