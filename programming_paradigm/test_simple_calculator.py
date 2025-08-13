import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 2), 5)
        self.assertEqual(self.calc.add(-3, -2), -5)
        self.assertEqual(self.calc.add(-3, 2), -1)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(-3, 2), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(-3, -2), 6)
        self.assertEqual(self.calc.multiply(-3, 2), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-3, -2), 1.5)
        self.assertEqual(self.calc.divide(-3, 2), -1.5)
        self.assertIsNone(self.calc.divide(10, 0))
