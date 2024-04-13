# This script calculates the dew point temperature and dew point spread given the relative humidity and temperature.
import argparse
def calculate_dew_point(relative_humidity, temperature):
    #Calculates the dew point temperature (only accurate over 50% RH)
    dew_point = temperature - ((100 - relative_humidity)/5)
    #Calculates the dew point spread from the current temperature
    dew_point_spread = dew_point - temperature
    return dew_point, dew_point_spread

#INPUTS:
#Relative humidity as a percentage
#Temperature in degrees Celsius

#OUTPUTS:
#Dew point temperature in degrees Celsius
#Dew point spread in degrees Celsius

#EXAMPLE:
#[dew_point, dew_point_spread] = calculate_dew_point(relative_humidity, temperature)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dew Point Calculator")
    parser.add_argument("relative_humidity", type=float, help="Relative humidity as a percentage")
    parser.add_argument("temperature", type=float, help="Temperature in degrees Celsius")
    args = parser.parse_args()

    relative_humidity = args.relative_humidity
    temperature = args.temperature

    # Check if pressure and altitude values are within acceptable range
    if relative_humidity < 0 or relative_humidity > 100:
        print("Invalid relative humidity value. Please enter a value between 0 and 100.")
    elif temperature < -50 or temperature > 60:
        print("Invalid temperature value. Please enter a value between -50 & 60.")
    else:
        [dew_point, dew_point_spread] = calculate_dew_point(relative_humidity, temperature)
        print("Dew Point Temperature:", dew_point)
        print("Dew Point Spread:", dew_point_spread)