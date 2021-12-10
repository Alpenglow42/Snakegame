import random

from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)

food_shapes = random.choice(["turtle", "square", "circle", "triangle"])
food_color = random.choice(["blue", "green", "yellow", "red", "orange"])


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(["turtle", "square", "circle", "triangle"]))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(["blue", "green", "yellow", "red", "orange"]))
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.shape(food_shapes)
        self.color(food_color)
        self.goto(random_x, random_y)

