# Firstly we ask for the user inputs
city_flight = input("Enter the city you will be flying to: ")
print("")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
print("")
rental_days = int(input("Enter the number of days that you will be hiring a car for: "))

# Secondly we define the pricing formulas for all four variables.

def hotel_cost(num_nights):
    # Thirdly we define a price per hotel night, and a multiplication operator with the user input.
    return 100 * num_nights

# Fourthly we select 3 cities and allocate return plane ticket prices, where if it is a different city we allocate 150 which I chose since it is the average European flight price. Also a multiplication operator with the user input.
def plane_cost(city_flight):
    if city_flight == "New York":
        return 500
    elif city_flight == "Paris":
        return 700
    elif city_flight == "Tokyo":
        return 1000
    else:
        return 150

# Fifthly we allocate a daily price for the car rental and a multiplication operator with the user input.
def car_rental(rental_days):
    # You can set your own daily rental cost
    return 50 * rental_days

#Sixthly we create a whole holiday Formula where all accounts added up return the whole holiday price
def holiday_cost(city_flight, num_nights, rental_days):
    # Call the three functions to get the total cost of the holiday
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# Seventhly the sum output gives the total holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Eighthly and finally the program prints out the separate and conjoing details about the holiday and the prices.
print("Your holiday details:")
print("")
print("City of flight: ", city_flight) 
print("")
print("Number of nights at hotel: ", num_nights) 
print("")
print("Number of rental days for car: ", rental_days)
print("")
print("Total cost: $", total_cost)