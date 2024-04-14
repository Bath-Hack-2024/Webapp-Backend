from datetime import datetime
import ephem
import math

def get_moon_phase(date: datetime):
    """
        Gets the current phase of the moon
    """
    
    moon = ephem.Moon()
    moon.compute(date.strftime('%Y/%m/%d'))
    moon_phase = moon.moon_phase
    
    phases = {
    0: "New Moon",
    0.25: "Waxing Crescent",
    0.5: "First Quarter",
    0.75: "Waxing Gibbous",
    1: "Full Moon",
    1.25: "Waning Gibbous",
    1.5: "Last Quarter",
    1.75: "Waning Crescent"
}

    # Find the closest phase based on the value
    closest_phase = min(phases, key=lambda x: abs(x - moon_phase))

    return phases[closest_phase]
def is_moon_visible(observer_lat, observer_lon, observation_time):
    """
    Determines if the moon is visible at a specific location and time.

    Args:
    - observer_lat (float): Latitude of the observer's location (in degrees).
    - observer_lon (float): Longitude of the observer's location (in degrees).
    - observation_time (datetime): Time of observation.

    Returns:
    - bool: True if the moon is visible, False otherwise.
    """

    # Create an observer object
    observer = ephem.Observer()
    observer.lat = str(observer_lat)
    observer.lon = str(observer_lon)
    observer.date = observation_time

    # Compute the moon's position
    moon = ephem.Moon(observer)

    # Check if the moon is above the horizon
    if moon.alt > 0:
        return True
    else:
        return False

