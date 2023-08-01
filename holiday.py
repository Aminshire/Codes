 
def hotel_cost(num_nights): # Returns the cost of the hotel room for the number of nights
    return 20 *num_nights

def plane_cost(city_flight): # Returns the cost of the flight to the chosen city
    if city_flight == 1:
        return 50
    elif city_flight == 2:
        return 250
    elif city_flight == 3:
        return 1000
    elif city_flight == 4:
        return 1200
    else:
        return 800

def car_rental(rental_days):# Returns the cost of hiring the car
    return 70 * rental_days

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

def end_message(city_flight): # Funtion telling the person to enjoy whatever city they're heading to
     return print(f"Enjoy your trip to {city_dict.get((city_flight))}!!!")

while True:
    # Creating a dictionary for the cities with the numbers as keys
    city_dict = {1:"Paris",2:"New York",3:"Tokyo",4:"Sdyney",5:"Rio De Janeiro"}
    try: # Making sure the input is only one of the 5 numbers
        city_flight = int(float(input("What city are you flying to?\nEnter the number of the corresponding city:\n1 - Paris\n2 - New York\n3 - Tokyo\n4 - Sydney\n5 - Rio De Janeiro \n:")))
        if city_flight == 1 :
            break
        elif city_flight == 2 :
            break
        elif city_flight == 3 :
            break
        elif city_flight == 4 :
            break
        elif city_flight == 5 :
            break
        else:
            print("Please only enter the number for the city")
            continue
    except ValueError:
        print("Please only enter the number for the city")
# Asking the number of nights staying and days for the hire
num_nights = int(input(f"How many nights will you be stay at {city_dict.get(city_flight)}?: "))
rental_days = int(input("How many days will you be hiring a car for?: "))

total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

print(f"\nYour flight to {city_dict.get(city_flight)} will cost £{plane_cost(city_flight)}")
if num_nights == 1:
    print(f"{num_nights} night at a hotel in {city_dict.get(city_flight)} will cost £{hotel_cost(num_nights)} ")
else:
    print(f"{num_nights} nights at a hotel in {city_dict.get(city_flight)} will cost £{hotel_cost(num_nights)} ")
if rental_days == 1:
        print(f"Hiring a car for {rental_days} day will cost £{car_rental(rental_days)}")
else:
        print(f"Hiring a car for {rental_days} days will cost £{car_rental(rental_days)}")
print(f"Your total for the holiday will be £{total_cost}")
end_message(city_flight)










