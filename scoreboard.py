from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.level = 0
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)


    def game_over(self):
        self.home()
        self.write(arg="Game Over!", align="center", font=FONT)
