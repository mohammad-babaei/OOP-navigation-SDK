from mapData.model.Way import Way
from typing import List


class Route:
    def __init__(self, ways: List[Way]):
        self.ways = ways

    def __str__(self):
        toReturn = "<Route> ways: ["
        for way in self.ways:
            toReturn += (str(way) + ", ")
        return toReturn + "]"
