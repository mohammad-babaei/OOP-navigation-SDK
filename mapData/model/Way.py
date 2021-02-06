from typing import List

from mapData.model.Node import Node


class Way:
    def __init__(self, ID, weight, nodes: List[Node], averageSpeed):
        self.id = ID
        self.weight = weight
        self.nodes = nodes
        self.averageSpeed = averageSpeed
