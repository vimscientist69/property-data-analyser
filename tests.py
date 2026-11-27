from analysis import calculate_average_price, find_most_expensive_property, find_cheapest_property, find_properties_per_location, calculate_average_price_per_location, filter_properties_by_minimum_price
import unittest

class TestAnalysisFunctions(unittest.TestCase):
    properties = [{"id": "P001", "price": 1_200_000, "bedrooms": 2, "location": "Sandton"},
        {"id": "P002", "price": 850_000, "bedrooms": 1, "location": "Randburg"},
        {"id": "P003", "price": 2_500_000, "bedrooms": 4, "location": "Sandton"},
        {"id": "P004", "price": 950_000, "bedrooms": 2, "location": "Randburg"},
        {"id": "P005", "price": 1_700_000, "bedrooms": 3, "location": "Sandton"},]

    def test_calc_avg_price(self):
        correct_avg_price = 1440000
        prices = [property["price"] for property in self.properties]
        avg_price = calculate_average_price(prices)
        self.assertEqual(avg_price, correct_avg_price, f"Avg price should be {correct_avg_price}.")

    def test_find_most_expensive_property(self):
        most_expensive_property = find_most_expensive_property(self.properties)
        self.assertEqual(most_expensive_property["id"], "P003", "Should match most expensive property ID number.")

    def test_cheapest_property(self):
        cheapest = find_cheapest_property(self.properties)
        self.assertEqual(cheapest["id"], "P002", "Should match cheapest property ID number.")

    def test_find_properties_per_location(self):
        properties_per_location = find_properties_per_location(self.properties)
        self.assertEqual(properties_per_location["Sandton"], 3, "Should find correct number of properties in Sandton")
        self.assertEqual(properties_per_location["Randburg"], 2, "Should find correct number of properties in Randburg")

if __name__ == "__main__":
    unittest.main()
