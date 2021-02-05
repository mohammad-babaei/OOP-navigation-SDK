from interface import implements, Interface
from entity import LocationLog


class LocationLogObserver(Interface):

    def onNewLocationLog(self, log: LocationLog):
        pass
