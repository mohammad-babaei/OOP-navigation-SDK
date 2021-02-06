from typing import List

from mapData.model.Node import Node


class Way:
    def __init__(self, weight, nodes: List[Node], averageSpeed):
        self.weight = weight
        self.nodes = nodes
        self.averageSpeed = averageSpeed
