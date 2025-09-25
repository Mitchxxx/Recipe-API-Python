"""
Sample Tests
"""


from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc module."""

    def test_add_numbers(self):
        res = calc.add(3, 6)
        self.assertEqual(res, 9)
        
    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
