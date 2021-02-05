from mapData import LatLng
from datetime import datetime


class LocationLog:

    def __init__(self, userId: str, location: LatLng, datetime, speed: float):
        self.userId = userId
        self.location = location
        self.datetime = datetime
        self.speed = speed
