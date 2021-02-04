from typing import List
from Way import Way
from Node import Node


class MapDataGraph:
    def __init__(self, edges: List[Way], vertices: List[Node]):
        self.edges = edges
        self.vertices = vertices
