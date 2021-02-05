from liveTraffic.entity.LocationLog import LocationLog
from mapData.LatLng import LatLng
from typing import List

class AnalyticsRepository:

    def __init__(self):
        # instantiate DB
        pass

    def saveLog(self, log: LocationLog):
        pass

    def getLogs(self, location: LatLng) -> List[LocationLog]:
        pass