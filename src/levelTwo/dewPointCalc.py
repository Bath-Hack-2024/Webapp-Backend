import math

def calculate_dew_point(relative_humidity, temperature):
    
    dew_point = temperature - ((100 - relative_humidity)/5)
    dew_point_spread = dew_point - temperature
    return dew_point, dew_point_spread

# Example usage
relative_humidity = float(input("Enter relative humidity (%): "))
temperature = float(input("Enter temperature (°C): "))

[dew_point, dew_point_spread] = calculate_dew_point(relative_humidity, temperature)
print("Dew point temperature: {:.2f}°C".format(dew_point))
print("Dew point spread: {:.2f}°C".format(dew_point_spread))
if dew_point_spread < -10:
    print("Probably foggy.")