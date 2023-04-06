import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating a screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Game")


# Creating turtle form the Turtle class
timmy = Player()

# creating a car object
car = CarManager()

# Creating the scoreboard class
score = Scoreboard()


# Adding event listeners to the screen
screen.listen()
screen.onkey(key="Up", fun= timmy.moveTurtle)

# Looping through the game every time the turtle moves

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    # Creating car objects only after 6 iterations of the loop
    if random.randint(1,6) ==1:
        car = CarManager()
    car.move_car()
    # Detecting collision between a car and a turtle
    collision_happens = timmy.detect_collisons()
    if collision_happens:
        game_is_on = False
        score.game_over()
    # Levelling Up
    if timmy.ycor() > 270:
        score.levelUp()
        car.speeding_car()
        timmy.resetting_Player()
        screen.clear()
        timmy = Player()
        screen.tracer(0)
        screen.listen()
        screen.onkey(key="Up", fun=timmy.moveTurtle)







screen.exitonclick()



