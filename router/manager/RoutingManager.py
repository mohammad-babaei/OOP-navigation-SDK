from ShortestPathAlgorithm import ShortestPathAlgorithm
from router.entity.BBox import BBox
from mapData.manager.MapDataManager import MapDataManager
from router.entity.Route import Route

class RoutingManager:
    def __init__(self, shortestPathAlgorithm: ShortestPathAlgorithm, mapDataManager: MapDataManager):
        self.algorithm = shortestPathAlgorithm
        self.mapDataManager = mapDataManager

    def findShortestPath(self, origin, destination) -> Route:
        smallestBBox = self.calculateSmallestBBox(origin, destination)

        mapDataGraph = self.mapDataManager.LoadMapDataGraph(smallestBBox)

        return self.algorithm.findShortestPath(mapDataGraph)

    def calculateSmallestBBox(self, firstLocation, SecondLocation) -> BBox:
        pass
