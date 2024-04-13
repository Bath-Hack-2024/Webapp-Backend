import numpy
#Function to nowcast the weather from pressure and altitude
def get_weather_rating(pressure, altitude):
    #Pressure and altitude conversion table
    altitude_pressure_conversion = numpy.array([
        [0, 1013.25],
        [100, 1011.25],
        [200, 1009.25],
        [300, 1007.25],
        [400, 1005.25],
        [500, 1003.25],
        [600, 1001.25],
        [700, 999.25],
        [800, 997.25],
        [900, 995.25],
        [1000, 993.25]
    ])
    altDiff = numpy.array([])
    #Find the closest altitude in the table to the current altitude
    for i in range(len(altitude_pressure_conversion)):
        altDiff = numpy.append(altDiff, numpy.absolute(altitude - altitude_pressure_conversion[i, 0]))
    #Find the pressure at the closest altitude
    pressureBackgroundInd = numpy.argmin(altDiff)
    pressureBackground = altitude_pressure_conversion[pressureBackgroundInd, 1]
    #Find the difference between the current pressure and the background pressure
    pressureDiff = pressure - pressureBackground
    return pressureDiff

#INPUTS:
#Pressure in hPa
#Altitude in metres above sea level
weather_rating = get_weather_rating(pressure, altitude)
#OUTPUTS:
#Difference in pressure from the background pressure at the closest altitude in the table

