from typing import List, Dict
import json
from analysis import calculate_average_price, find_most_expensive_property, find_cheapest_property, find_properties_per_location, calculate_average_price_per_location, filter_properties_by_minimum_price

def main():
    properties = [
        {"id": "P001", "price": 1_200_000, "bedrooms": 2, "location": "Sandton"},
        {"id": "P002", "price": 850_000, "bedrooms": 1, "location": "Randburg"},
        {"id": "P003", "price": 2_500_000, "bedrooms": 4, "location": "Sandton"},
        {"id": "P004", "price": 950_000, "bedrooms": 2, "location": "Randburg"},
        {"id": "P005", "price": 1_700_000, "bedrooms": 3, "location": "Sandton"},
    ]
    prices = [property["price"] for property in properties]
    average_price = calculate_average_price(prices) if len(prices) > 0 else 0

    most_expensive = find_most_expensive_property(properties)
    cheapest = find_cheapest_property(properties)
    properties_per_location = find_properties_per_location(properties)
    average_price_per_location = calculate_average_price_per_location(properties)
    
    minimum_price = 1000000
    filter_by_minimum_price = filter_properties_by_minimum_price(minimum_price, properties)

    return { "avg_price": average_price, "most_expensive": most_expensive, "cheapest": cheapest, "properties_per_location": find_properties_per_location, "average_price_per_location": average_price_per_location, "filter_by_minimum_price": filter_properties_by_minimum_price }

if __name__ == "__main__":
    result = main()
