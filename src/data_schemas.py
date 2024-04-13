weather_station_upload_schema = {
    "type": "object",
    "properties": {
        "lat": {"type": "number"},
        "lon": {"type": "number"},
        "elevation": {"type": "number"},
        "station_id": {"type": "string"},
        "temperature": {"type": "number"},
        "humidity": {"type": "number"},
        "barometric_pressure": {"type": "number"},
    },
    "required": ["lat", "lon", "station_id", ]
}