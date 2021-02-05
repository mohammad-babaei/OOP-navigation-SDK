from typing import List

from liveTraffic.LocationLogObserver import LocationLogObserver
from liveTraffic.entity.LocationLog import LocationLog


class LiveLocationService:

    def __init__(self, observers: List[LocationLogObserver]):
        self.observers = observers

    def sendLocation(self, log: LocationLog):
        for observer in self.observers:
            observer.onNewLocationLog(log)

    def subscribe(self, observer: LocationLogObserver):
        self.observers.append(observer)