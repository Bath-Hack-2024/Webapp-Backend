# This script calculates the dew point temperature and dew point spread given the relative humidity and temperature.
def calculate_dew_point(relative_humidity, temperature):
    '''
    Calculates the dew point temperature and dew point spread given the relative humidity and temperature.

    Parameters:
    relative_humidity (float): Relative humidity as a percentage
    temperature (float): Temperature in degrees Celsius

    Returns:
    dew_point (float): Dew point temperature in degrees Celsius
    dew_point_spread (float): Dew point spread in degrees Celsius

    Example:
    [dew_point, dew_point_spread] = calculate_dew_point(relative_humidity, temperature)
    '''
    #Checks if the inputs are floats and are within the valid range
    if type(relative_humidity) != float or type(temperature) != float:
        print("Invalid input type. Please enter a float value.")
        raise TypeError

    if relative_humidity < 0 or relative_humidity > 100:
        print("Invalid relative humidity value. Please enter a value between 0 and 100.")
        raise ValueError 
    elif temperature < -50 or temperature > 60:
        print("Invalid temperature value. Please enter a value between -50 & 60.")
        raise ValueError
    
    #Calculates the dew point temperature (only accurate over 50% RH)
    dew_point = temperature - ((100 - relative_humidity)/5)
    #Calculates the dew point spread from the current temperature
    dew_point_spread = dew_point - temperature
    return dew_point, dew_point_spread