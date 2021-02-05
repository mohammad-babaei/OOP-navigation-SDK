from enum import Enum
from typing import Dict


class ReportType(Enum):
    Accident = 'Accident'
    Police = 'Police'
    Camera = 'Camera'


class Report:
    def __init__(self, dateTime, reportType: ReportType, location, properties: Dict):
        self.dateTime = dateTime
        self.reportType = reportType
        self.location = location
        self.properties = properties


