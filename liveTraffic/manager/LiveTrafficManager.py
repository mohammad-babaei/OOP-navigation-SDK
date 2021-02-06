from liveTraffic.LocationLogObserver import LocationLogObserver
from liveTraffic.entity.LocationLog import LocationLog
from mapData.repository.MapDataRepository import MapDataRepository


class LiveTrafficManager(LocationLogObserver):

    def __init__(self, mapDataRepository: MapDataRepository):
        self.mapDataRepository = mapDataRepository

    def onNewLocationLog(self, log: LocationLog):
        # Update traffic
        wayId = self.mapDataRepository.findWayByLocation(log.location).id
        self.mapDataRepository.updateWaySpeed(wayId, log.speed)