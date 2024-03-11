import unittest
from simulation import Simulator
from field import Field
from car import Car


class TestCollisionDetection(unittest.TestCase):

    def test_two_car_collision(self):
        field = Field(10, 10)
        simulator = Simulator(field)
        simulator.add_car_simulator("A", 1, 2, "N", "FFRFFFFRRL")
        simulator.add_car_simulator("B", 7, 8, "W", "FFLFFFFFFF")

        # Trigger collision detection (adjust if needed)
        simulator.run_simulation()

        expected_collision = {(5, 4): {"step": 7, "cars": {"A", "B"}}}

        self.assertEqual(simulator.collided_cars, expected_collision)

    def test_three_car_collision(self):
        field = Field(3, 3)
        simulator = Simulator(field)
        simulator.add_car_simulator("CarA", 0, 0, "N", "FRF")
        simulator.add_car_simulator("CarB", 2, 2, "S", "FRF")
        simulator.add_car_simulator("CarC", 0, 2, "E", "FRF")

        # Trigger collision detection (adjust if needed)
        simulator.run_simulation()

        expected_collision = {(1, 1): {"step": 3, "cars": {"CarA", "CarB", "CarC"}}}

        self.assertEqual(simulator.collided_cars, expected_collision)


class TestSimulator(unittest.TestCase):

    def test_add_car(self):
        field = Field(10, 10)
        simulator = Simulator(field)

        simulator.add_car_simulator("Car1", 2, 3, "E", "FFR")
        self.assertEqual(len(simulator.cars), 1)
        self.assertEqual(simulator.cars[0].name, "Car1")

    def test_detect_collisions(self):
        field = Field(5, 5)
        simulator = Simulator(field)
        # Manually set up cars in a colliding state
        simulator.cars = [Car("A1", 3, 3, "N"), Car("B2", 3, 3, "W")]
