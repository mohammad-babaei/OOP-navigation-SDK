from mapData.model.Way import Way
from typing import List


class Route:
    def __init__(self, ways: List[Way]):
        self.ways = ways
