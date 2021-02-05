from typing import List
from mapData.model.Way import Way
from mapData.model.Node import Node


class MapDataGraph:
    def __init__(self, edges: List[Way], vertices: List[Node]):
        self.edges = edges
        self.vertices = vertices
