import unittest
from car_simulation.car import Car
from car_simulation.field import Field


# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestCar(unittest.TestCase):
    def test_move_forward_within_bounds(self):
        car = Car("A", 2, 3, "N")
        field = Field(10, 10)
        car.move_forward(field)
        print(self.assertEqual(car.x, 2))
        self.assertEqual(car.y, 4)

    def test_move_forward_out_of_bounds(self):
        car = Car("B", 9, 9, "E")
        field = Field(10, 10)
        car.move_forward(field)
        self.assertEqual(car.x, 9)
        self.assertEqual(car.y, 9)

    def test_turn_left(self):
        car = Car("C", 0, 0, "N")
        car.turn_left()
        self.assertEqual(car.direction, "W")

    def test_turn_right(self):
        car = Car("D", 0, 0, "S")
        car.turn_right()
        self.assertEqual(car.direction, "W")


if __name__ == "__main__":
    unittest.main()
