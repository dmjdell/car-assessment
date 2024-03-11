import unittest
from car_simulation.field import Field


class TestField(unittest.TestCase):

    def test_within_bounds(self):
        grid = Field(5, 10)  # Create a test field

        # Test within boundaries
        self.assertTrue(grid.is_within_bounds(2, 5))
        self.assertTrue(grid.is_within_bounds(0, 0))  # Test edges
        self.assertTrue(grid.is_within_bounds(4, 9))  # Test edges

    def test_out_of_bounds(self):
        grid = Field(5, 10)

        # Test out of bounds (negative coordinates)
        self.assertFalse(grid.is_within_bounds(-1, 5))
        self.assertFalse(grid.is_within_bounds(2, -3))

        # Test out of bounds (coordinates too large)
        self.assertFalse(grid.is_within_bounds(5, 3))
        self.assertFalse(grid.is_within_bounds(2, 10))
