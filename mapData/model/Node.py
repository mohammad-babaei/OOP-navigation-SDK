class Node:
    def __init__(self, ID: int, lat: float, lon: float):
        self.id = ID
        self.lat = lat
        self.lon = lon

    def getId(self) -> int:
        return self.id

    def getLat(self) -> float:
        return self.lat

    def getLon(self) -> float:
        return self.lon
