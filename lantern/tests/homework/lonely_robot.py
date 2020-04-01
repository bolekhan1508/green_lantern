
class Asteroid:

    def __init__(self, x, y):

        self.x = x
        self.y = y


class Robot:

    def __init__(self, x, y, asteroid, direction):

        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        self.check_robot_miss_asteroid()

    def turn_left(self):

        turns = {
            'N': 'W',
            'W': 'S',
            'S': 'E'}

        self.direction = turns[self.direction]

    def turn_right(self):

        turns = {
            "N": "E",
            "W": "N",
            "S": "W",
            "E": "S"}

        self.direction = turns[self.direction]

    def move_forward(self):

        dict_move_forward = {
            'N': (self.x, self.y + 1),
            'W': (self.x - 1, self.y),
            'S': (self.x, self.y - 1),
            'E': (self.x + 1, self.y)
        }

        self.x, self.y = dict_move_forward[self.direction]

    def move_backward(self):

        dict_move_backward = {
            'N': (self.x, self.y - 1),
            'W': (self.x + 1, self.y),
            'S': (self.x, self.y + 1),
            'E': (self.x - 1, self.y)
        }

        self.x, self.y = dict_move_backward[self.direction]

    def check_robot_miss_asteroid(self):

        if self.x > self.asteroid.x or self.x < 0 or self.y > self.asteroid.y or self.y < 0:
            raise MissAsteroidError()

    def check_robot_location(self):

        if self.x > self.asteroid.x or self.x < 0 or self.y > self.asteroid.y or self.y < 0:
            raise MovingError()


class MissAsteroidError(Exception):
    pass


class MovingError(Exception):
    pass
