from turtle import Turtle
import car_manager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def moveTurtle(self):
        self.forward(MOVE_DISTANCE)

    def detect_collisons(self):
        for i in range(len(car_manager.all_cars)):
            if self.distance(car_manager.all_cars[i]) < 20:
                return True
        return False

    def resetting_Player(self):
        self.goto(0, -280)








