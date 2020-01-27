import unittest

from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_county_city(self):
        formatted_City = city_country('America', 'New York')
        self.assertEqual(formatted_City, 'America, New York')

    def test_county_city_population(self):
        formatted_City = city_country('America', 'New York', '9000000000')
        self.assertEqual(formatted_City, 'America, New York - population 9000000000')
