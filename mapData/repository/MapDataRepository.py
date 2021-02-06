from mapData.entity.LatLng import LatLng
from mapData.model.Node import Node
from mapData.model.Way import Way
from typing import List

from router.entity.BBox import BBox


class MapDataRepository:
    def addNode(self, node: Node):
        pass

    def addWay(self, way: Way):
        pass

    def updateWayWeight(self, wayID: int):
        pass

    def updateWaySpeed(self, wayID: int):
        pass

    def findWayByLocation(self, location: LatLng) -> Way:
        pass

    def GetWaysInBBox(self, bbox: BBox) -> List[Way]:
        pass

    def GetNodesInBbox(self, bbox: BBox) -> List[Way]:
        pass
