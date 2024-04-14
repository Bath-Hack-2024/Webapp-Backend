from data_science.now_cast import get_weather_nowcast_pressure
from data_science.dew_point import calculate_dew_point
from data_science.moon import get_moon_phase, is_moon_visible

from datetime import datetime

def add_l2_data(data):
    for station in data:
        data_points = data[station]

        for point in data_points:
            humidity = float(point.get('humidity'))
            temperature = float(point.get('temperature'))
            barometric_pressure = float(point.get('barometric_pressure'))
            elevation = float(point.get('elevation'))

            try:
                now_cast = get_weather_nowcast_pressure(barometric_pressure, elevation)
            except Exception as e:
                now_cast = None

            try:
                dew_point, dew_point_spread = calculate_dew_point(humidity, temperature)
            except Exception as e:
                dew_point = None
                dew_point_spread = None

            try:
                date = datetime.strptime(point['time_stamp'], "%m/%d/%Y, %H:%M:%S")
                moon_phase = get_moon_phase(date)
                moon_visible = is_moon_visible(elevation, elevation, date)

                print(date)
            except Exception as e:
                moon_phase = None
                moon_visible = None

            point['now_cast'] = now_cast
            point['dew_point'] = dew_point
            point['dew_point_spread'] = dew_point_spread
            point['moon_phase'] = moon_phase
            point['moon_visible'] = moon_visible


    return data


