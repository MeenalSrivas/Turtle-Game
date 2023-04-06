from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars = []


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        self.random_location()
        all_cars.append(self)

    def randomly_generating_y(self):
        return random.randint(-250, 250)

    def random_location(self):
        random_y = self.randomly_generating_y()
        if len(all_cars) > 4:
            keep_generating = True
            while keep_generating:
                j = 0
                for i in range(len(all_cars)-1, len(all_cars)-5, -1):
                    if abs(random_y - all_cars[i].ycor()) < 44:
                        j += 1
                        break
                if j == 0:
                    break
                random_y = self.randomly_generating_y()
        self.goto(300, random_y)

    def move_car(self):
        for obj in all_cars:
            obj.forward(STARTING_MOVE_DISTANCE)

    def speeding_car(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        self.resetting_game()

    def resetting_game(self):
        global all_cars
        while len(all_cars) != 0:
            del all_cars[0]
        all_cars = []







