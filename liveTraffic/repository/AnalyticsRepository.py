from datetime import datetime

from liveTraffic.model.LocationLog import LocationLog
from mapData.entity.LatLng import LatLng

from typing import List


class AnalyticsRepository:

    def __init__(self):
        # instantiate DB
        pass

    def saveLog(self, log: LocationLog):
        print('log {} was saved'.format(log))

    def getLogs(self, location: LatLng) -> List[LocationLog]:
        return [LocationLog(userId='1', location=LatLng(1.0, 1.0), datetime=datetime.now(), speed=1.0)]
