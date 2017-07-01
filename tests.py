# TODO place your tests here
import unittest
from format_price import format_price


class PriceFormatTestCase(unittest.TestCase):
    def test_first_case(self):
        result = format_price(1234)
        self.assertEqual(result, '1 234')


    def test_second_case(self):
        result = format_price(1234.0)
        self.assertEqual(result, '1 234')

    def test_third_case(self):
        result = format_price(1234.01)
        self.assertEqual(result, '1 234.01')
        

    def test_fours_case(self):
        with self.assertRaises(ValueError):
            format_price([1234])

 
