from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        x_cor = self.xcor() 
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(x=x_cor, y=y_cor)


    def next_level(self):
        self.goto(STARTING_POSITION)
