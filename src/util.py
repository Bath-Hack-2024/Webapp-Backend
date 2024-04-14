from data_science.now_cast import get_weather_nowcast_pressure

def add_l2_data(data):
    for station in data:
        data_points = data[station]

        for point in data_points:
            humidity = point.get('humidity')
            temperature = point.get('temperature')
            barometric_pressure = float(point.get('barometric_pressure'))
            elevation = float(point.get('elevation'))

            try:
                now_cast = get_weather_nowcast_pressure(barometric_pressure, elevation)
            except Exception as e:
                now_cast = None

            
            
            point['now_cast'] = now_cast

    return data


