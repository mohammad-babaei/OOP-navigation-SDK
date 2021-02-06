from interface import implements, Interface

from mapData.model.Node import Node
from mapData.model.Way import Way
from router.entity.Route import Route


# define the interface
class ShortestPathAlgorithm(Interface):
    def findShortestPath(self, MapDataGraph) -> Route:
        pass


# now classes implement the interface
class Dijkstra(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph) -> Route:
        return Route([
            Way(1, 2, [Node(1, 51.65465, 37.5465), Node(2, 20.65465, 15.5465)], 30.2),
            Way(2, 10, [Node(3, 40.65465, 75.5465), Node(4, 65.65465, 21.5465)], 50.2),
        ])
        pass


class FloydWarshall(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph) -> Route:
        pass


class BellmanFord(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph) -> Route:
        pass
