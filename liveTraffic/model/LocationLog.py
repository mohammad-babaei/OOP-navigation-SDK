from mapData.entity.LatLng import LatLng
from datetime import datetime


class LocationLog:

    def __init__(self, userId: str, location: LatLng, datetime: datetime, speed: float):
        self.userId = userId
        self.location = location
        self.datetime = datetime
        self.speed = speed

    def getUserId(self) -> str:
        return self.userId

    def getLocation(self) -> LatLng:
        return self.location

    def getDateTime(self) -> datetime:
        return self.datetime

    def getSpeed(self) -> float:
        return self.speed
