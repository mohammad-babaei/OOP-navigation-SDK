from typing import List

from mapData.model.Node import Node


class Way:
    def __init__(self, weight, nodes: List[Node]):
        self.weight = weight
        self.nodes = nodes
