from mapData.repository.MapDataRepository import MapDataRepository
from router.entity.BBox import BBox
from mapData.entity.MapDataGarph import MapDataGraph


class MapDataManager:
    def __init__(self, mapDataRepository: MapDataRepository):
        self.mapDataRepository = mapDataRepository

    def LoadMapDataGraph(self, bbox: BBox) -> MapDataGraph:
        pass
