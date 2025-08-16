from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_chance = random.randrange(1, 8)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.color(random.choice(COLORS))
            new_cars.penup()
            new_cars.shapesize(1,2)
            random_y = random.randint(-250,250)
            new_cars.goto(300,random_y)
            self.all_cars.append(new_cars)

    def move(self):
        for car in self.all_cars:
            car.forward(-1 * STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
