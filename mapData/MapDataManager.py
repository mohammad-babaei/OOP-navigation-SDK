from MapDataRepository import MapDataRepository
from router.BBox import BBox
from MapDataGarph import MapDataGraph


class MapDataManager:
    def __init__(self, mapDataRepository: MapDataRepository):
        self.mapDataRepository = mapDataRepository

    def LoadMapDataGraph(self, bbox: BBox) -> MapDataGraph:
        pass
