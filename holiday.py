def hotel_cost(num_nights):
    """Calculate the cost of hotel stay."""
    # Assume a cost of $150 per night
    return num_nights * 150

def plane_cost(city_flight):
    """Calculate the cost of flight."""
    # Define prices for different cities
    if city_flight == 'New York':
        return 500
    elif city_flight == 'Paris':
        return 300
    elif city_flight == 'Tokyo':
        return 800
    else:
        return 0  # for invalid input

def car_rental(rental_days):
    """Calculate the cost of car rental."""
    # Assume a cost of $65 per day
    return rental_days * 65

def holiday_cost(num_nights, city_flight, rental_days):
    """Calculate the total cost of the holiday."""
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# Get user inputs
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car for: "))

# Calculate the total cost of the holiday
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print out the details about the holiday
print("Holiday details:")
print("City of flight:", city_flight)
print("Number of nights at hotel:", num_nights)
print("Number of days renting a car:", rental_days)
print("Total cost of holiday: $", total_cost)