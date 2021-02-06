from typing import List

from mapData.model.Node import Node


class Way:
    def __init__(self, ID: int, weight: float, nodes: List[Node], averageSpeed: float):
        self.id = ID
        self.weight = weight
        self.nodes = nodes
        self.averageSpeed = averageSpeed

    def getId(self) -> int:
        return self.id

    def getNodes(self) -> List[Node]:
        return self.nodes

    def getWeight(self) -> float:
        return self.weight

    def getAverageSpeed(self) -> float:
        return self.averageSpeed