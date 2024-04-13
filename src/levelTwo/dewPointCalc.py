# This script calculates the dew point temperature and dew point spread given the relative humidity and temperature.

def calculate_dew_point(relative_humidity, temperature):
    #Calculates the dew point temperature (only accurate over 50% RH)
    dew_point = temperature - ((100 - relative_humidity)/5)
    #Calculates the dew point spread from the current temperature
    dew_point_spread = dew_point - temperature
    return dew_point, dew_point_spread

#INPUTS:
#Relative humidity as a percentage
#Temperature in degrees Celsius
[dew_point, dew_point_spread] = calculate_dew_point(relative_humidity, temperature)
#OUTPUTS:
#Dew point temperature in degrees Celsius
#Dew point spread in degrees Celsius