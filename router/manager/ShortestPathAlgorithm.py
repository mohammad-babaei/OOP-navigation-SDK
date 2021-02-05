from interface import implements, Interface
from router.entity.Route import Route


# define the interface
class ShortestPathAlgorithm(Interface):
    def findShortestPath(self, MapDataGraph) -> Route:
        pass


# now classes implement the interface
class Dijkstra(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph) -> Route:
        pass


class FloydWarshall(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph) -> Route:
        pass


class BellmanFord(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph) -> Route:
        pass
