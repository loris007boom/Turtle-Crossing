from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 2.5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        random_color = random.choice(COLORS)
        self.penup()
        self.color(random_color)
        self.shapesize(stretch_wid=1, stretch_len=2)





class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = 10
        for _ in range(10):
            car = Car()
            car.goto(self.random_cor(), self.random_cor())
            self.cars.append(car)


    def spawn_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                new_car = Car()
                new_car.goto(280, self.random_cor())
                self.cars.append(new_car)
                car.hideturtle()
                self.cars.remove(car)
                


    def move(self):
        for car in self.cars:
            x_cor = car.xcor() - self.move_distance
            y_cor = car.ycor() 
            car.goto(x_cor, y_cor)


    def random_cor(self):
        return random.randint(-250, 291)


    def next_level(self):
        self.move_distance += MOVE_INCREMENT
