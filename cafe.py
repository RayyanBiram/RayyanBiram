# Define the menu list
menu = ["coffee", "croissant", "sandwich", "panini"]

# Define the stock dictionary
stock = {
    "coffee": 50,
    "croissant": 20,
    "sandwich": 30,
    "panini": 40
}

# Define the price dictionary
price = {
    "coffee": 2.5,
    "croissant": 2.0,
    "sandwich": 5.0,
    "panini": 4.5
}

# Calculate the total stock value
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# Print the total stock value
print("The total stock value is: ${:.2f}".format(total_stock))