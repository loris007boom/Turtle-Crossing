from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

FINISH_LINE_Y = 280

#Screen setup
screen = Screen()
screen.setup(width=600, height=600)


def main_game():
    #Screen setup reset
    screen.tracer(0)

    #Objects initialization
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    #Screen listening for inputs
    screen.listen()
    screen.onkey(key="Up", fun=player.move)

    #Main game
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.move()
        car_manager.spawn_cars()

        #Detect collision with finish line
        if player.ycor() > FINISH_LINE_Y:
            player.next_level()
            car_manager.next_level()
            scoreboard.update_score()

        #Detect collision with cars
        for car in car_manager.cars:
            if player.distance(car) < 30:
                scoreboard.game_over()
                screen.update()
                game_is_on = False
                time.sleep(1)
                screen.clearscreen()
                main_game()





main_game()






screen.exitonclick()
