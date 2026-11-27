from typing import List, Dict
import json

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

    return

def filter_properties_by_minimum_price(minimum_price: int, properties: List[Dict[str: str]]):
    return list(filter(lambda x: x["price"] >= minimum_price, properties))

def calculate_average_price(prices: List[int]):
    return sum(prices) / len(prices)

def calculate_average_price_per_location(properties: List[Dict[str: str]]):
    properties_prices_grouped_by_location : Dict[str: List[int]] = {}
    for property in properties:
        location = property["location"]
        if location not in properties_prices_grouped_by_location:
            properties_prices_grouped_by_location[location] = [property["price"]]
        else:
            properties_prices_grouped_by_location[location].append(property["price"])

    average_prices = {}
    for key in properties_prices_grouped_by_location.keys():
        average_prices[key] = calculate_average_price(properties_prices_grouped_by_location[key])
    return average_prices

def find_properties_per_location(properties: List[Dict[str: str]]):
    location_map = {}
    for property in properties:
        location = property["location"]
        if location not in location_map:
            location_map[location] = 1
        else:
            location_map[location] = location_map[location] + 1

    return location_map

def find_cheapest_property(properties: List[Dict[str: str]]):
    cheapest = {"price": 0}

    for property in properties:
        if property["price"] < cheapest["price"]:
            cheapest = property

    return cheapest

def find_most_expensive_property(properties: List[Dict[str: str]]):
    most_expensive = {"price": 0}

    for property in properties:
        if property["price"] > most_expensive["price"]:
            most_expensive = property

    return most_expensive

main()
