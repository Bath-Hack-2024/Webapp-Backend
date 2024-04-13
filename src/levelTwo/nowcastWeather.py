import numpy
def get_weather_rating(pressure, altitude):
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
    for i in range(len(altitude_pressure_conversion)):
        #print(i)
        altDiff = numpy.append(altDiff, numpy.absolute(altitude - altitude_pressure_conversion[i, 0]))

    pressureBackgroundInd = numpy.argmin(altDiff)
    pressureBackground = altitude_pressure_conversion[pressureBackgroundInd, 1]
    print(pressureBackground)
    pressureDiff = pressure - pressureBackground
    print(pressureDiff)
    if pressureDiff < -10:
        return "stormy"
    elif pressureDiff < -5:
        return "rainy"
    elif pressureDiff < 5:
        return "cloudy"
    elif pressureDiff < 10:
        return "sunny"
    else:
        return "clear"
# Example usage
pressure_measurement = 1000
altitude = 180
weather_rating = get_weather_rating(pressure_measurement, altitude)
print(f"The weather rating is: {weather_rating}")

