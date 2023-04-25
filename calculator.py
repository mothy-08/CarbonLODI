from miscellaneous import ErrorHandler


class CarbonEmission:
    def __init__(self, current_user):
        self.filename = f"user-{current_user}.txt"  # names '.txt' files for each user

    @staticmethod
    def housing_emissions():  # Ask user for housing information
        house_size_sq_m = ErrorHandler.get_float("Size of your house (square meters): ")
        occupants = ErrorHandler.get_int("Number of occupants in your house: ")
        electricity_use = ErrorHandler.get_float("Electric consumption per month (kWH): ")
        lpg_use = ErrorHandler.get_float("Estimate the number of days your 11 kg LPG lasts: ")

        #  Formulas per month
        house_size_sq_ft = house_size_sq_m * 10.764  # 1 sq m = 10.764 sq ft
        electricity_emissions = electricity_use * 0.5  # 0.5 kg CO2e per kWH
        lpg_emissions = (35 / lpg_use) * 30  # 35 CO2e = (30 per LPG cylinder) + (5 average CO2e of stove per Cylinder)

        # Convert to grams per day
        return ((electricity_emissions + lpg_emissions) / occupants / house_size_sq_ft) * 1000 / 30

    @staticmethod
    def transportation_emissions():
        transportation_type = ErrorHandler.get_valid_option('''
        Your form of transportation 
        0 - Walking
        1 - Private Vehicle
        2 - Public Vehicle

        Response: 
        ''', ['0', '1', '2'])

        if transportation_type == '0':
            transportation_co2e = 0  # No emissions for walking
        elif transportation_type == '1':
            passengers = ErrorHandler.get_int("Number of people in the vehicle: ")
            distance = ErrorHandler.get_float("Distance of your transportation (km): ")
            fuel_efficiency = ErrorHandler.get_float("What is the fuel efficiency of the vehicle (in km/L)? ")
            fuel_type = input("What type of fuel does the vehicle use? (1 - Gasoline / 2 - Diesel) ")
            emissions_factor = 2352.7 if fuel_type == '1' else 2639.4 if fuel_type == '2' else 0
            transportation_co2e = (emissions_factor * distance / fuel_efficiency) / passengers
        elif transportation_type == '2':
            distance = ErrorHandler.get_float("Distance of your transportation (km): ")
            transportation_co2e = 90 * distance  # 90 g CO2e/km/passenger on average for public transportation
        else:
            print("Sorry, we didn't understand your transportation type.")
            transportation_co2e = 0

        return transportation_co2e

    @staticmethod
    def food_emissions():
        emissions_dict = {}
        with open("food.txt") as f:
            for line in f:
                food, emissions = line.strip().split(":")
                emissions_dict[food] = float(emissions)
        food_items = []
        while True:
            food_item = input("Enter a food item you ate today (or 'done' if finished): ")
            if food_item == 'done':
                break
            else:
                food_items.append(food_item)

        food_co2e = 0
        for food_item in food_items:
            if food_item in emissions_dict:
                servings = ErrorHandler.get_float(f"Your servings of {food_item} (grams) ")
                food_co2e += (servings * emissions_dict[food_item])
            else:
                print(f"Sorry, we don't have emissions data for {food_item}. Skipping...")
        return food_co2e

    def calculate_all(self):
        total_emissions = self.housing_emissions() + self.transportation_emissions() + self.food_emissions()
        with open(self.filename, 'a') as file:
            file.write(f"Today's Emission: {total_emissions:.2f} g/day\n")


