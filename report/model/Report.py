from enum import Enum
from typing import Dict

from mapData.entity.LatLng import LatLng


class ReportType(Enum):
    Accident = 'Accident'
    Police = 'Police'
    Camera = 'Camera'


class Report:
    def __init__(self, dateTime, reportType: ReportType, location: LatLng, properties: Dict):
        self.dateTime = dateTime
        self.reportType = reportType
        self.location = location
        self.properties = properties

    def __str__(self):
        return "<Report> dateTime: " + str(self.dateTime) + " reportType: " + str(
            self.reportType) + " location: " + str(self.location)
