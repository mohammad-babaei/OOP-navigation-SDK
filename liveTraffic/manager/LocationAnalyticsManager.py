from liveTraffic.LocationLogObserver import LocationLogObserver
from liveTraffic.entity.LocationLog import LocationLog
from liveTraffic.repository.AnalyticsRepository import AnalyticsRepository


class LocationAnalyticsManager(LocationLogObserver):

    def __init__(self, analyticsRepository: AnalyticsRepository):
        self.analyticsRepository = analyticsRepository

    def onNewLocationLog(self, log: LocationLog):
        self.analyticsRepository.saveLog(log)