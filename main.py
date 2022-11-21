import random
import turtle


from turtle import  Turtle,Screen


turtle.colormode(255)
my_screen = Screen()


tom = Turtle()
tom.penup()
tom.hideturtle()
tom.speed("fastest")


# color = colorgram.extract("hirst.jpg", 180)
# rgb_list = []
# for k in color:
#     r = k.rgb.r
#     g = k.rgb.g
#     b = k.rgb.b
#
#     rgb = (r,g,b)
#     rgb_list.append(rgb)
# rgb_list = rgb_list[4:]

color_list = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90), (49, 42, 47), (34, 61, 56), (227, 165, 169), (170, 188, 221), (184, 103, 112), (32, 59, 108), (105, 127, 160), (175, 200, 188), (33, 150, 210), (65, 66, 56), (35, 78, 89), (106, 139, 124), (152, 201, 229), (146, 125, 107)]


tom.setheading(220)
tom.forward(400)
tom.setheading(0)

def draw(n):

    for k in range(1,n+1):

      tom.dot(20,random.choice(color_list))
      tom.forward(50)

      if k%10 == 0:

          tom.left(90)
          tom.forward(50)
          tom.left(90)
          tom.forward(500)
          tom.setheading(0)


#
#
# def d1():
#     tom.left(90)
#     tom.forward(50)
#     tom.setheading(180)
#     tom.forward(100)
#
#
#
# def d2():
#     tom.right(90)
#     tom.forward(50)
#     tom.setheading(0)
#     tom.forward(50)

# for _ in range(5):
#
#     draw()
#
#     d1()
#
#     draw()
#
#     d2()
number_of_dots = 100
draw(number_of_dots)


my_screen.exitonclick()