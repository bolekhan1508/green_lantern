
import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError, MovingError


class TestRobotCreating:

    def test_parameters(self):
        x = 12
        y = 23
        asteroid = Asteroid(x, y)

        direction = 'E'
        robot = Robot(x, y, asteroid, direction)

        assert robot.x == 12
        assert robot.y == 23
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((12, 23), (24, 29)),
                ((12, 23), (24, 23)),
                ((12, 23), (12, 26)),
        )
    )
    def test_check_robot_on_asteroid(self, asteroid_size, robot_coordinates):

        with pytest.raises(MissAsteroidError):

            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, 'W')


class TestMove:

    def setup(self):
        self.x, self.y = 15, 25
        self.asteroid = Asteroid(self.x, self.y)
        self.direction = 'N'

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ('N', 'W'),
                ('W', 'S'),
                ('S', 'E'),
        )
    )
    def test_turn_left(self, current_direction, expected_direction):

        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()

        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ('N', 'E'),
                ('E', 'S'),
                ('S', 'W'),
        )
    )
    def test_turn_right(self, current_direction, expected_direction):

        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()

        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, current_x, current_y ,expected_x, expected_y",
        (
                ('N', 8, 8, 8, 9),
                ('W', 0, 8, -1, 8),
                ('S', 8, 0, 8, -1),
                ('E', 8, 8, 9, 8)
        )
    )
    def test_move_forward(self, current_direction, current_x, current_y, expected_x, expected_y):

        asteroid = Asteroid(8, 8)
        robot = Robot(current_x, current_y, asteroid, current_direction)

        assert robot.x == current_x and robot.y == current_y
        robot.move_forward()

        assert robot.x == expected_x and robot.y == expected_y
        with pytest.raises(MovingError):
            robot.check_robot_location()

    @pytest.mark.parametrize(
        "current_direction, current_x, current_y ,expected_x, expected_y",
        (
                ('N', 8, 0, 8, -1),
                ('W', 8, 8, 9, 8),
                ('S', 8, 8, 8, 9),
                ('E', 0, 8, -1, 8)
        )
    )
    def test_move_backward(self, current_direction, current_x, current_y, expected_x, expected_y):

        asteroid = Asteroid(8, 8)
        robot = Robot(current_x, current_y, asteroid, current_direction)

        assert current_x == robot.x and current_y == robot.y
        robot.move_backward()

        assert robot.x == expected_x and robot.y == expected_y
        with pytest.raises(MovingError):
            robot.check_robot_location()
