from interface import implements, Interface


# define the interface
class ShortestPathAlgorithm(Interface):
    def findShortestPath(self, MapDataGraph):
        pass


# now classes implement the interface
class Dijkstra(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph):
        pass


class FloydWarshall(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph):
        pass


class BellmanFord(implements(ShortestPathAlgorithm)):
    def findShortestPath(self, MapDataGraph):
        pass

