from enum import Enum


class ReportType(Enum):
    Accident = 'Accident'
    Police = 'Police'
    Camera = 'Camera'


class Report:
    def __init__(self, dateTime, reportType: ReportType, location, properties):
        self.dateTime = dateTime
        self.reportType = reportType
        self.location = location
        self.properties = properties


