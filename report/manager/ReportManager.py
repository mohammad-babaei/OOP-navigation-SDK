from typing import List

from mapData.entity.LatLng import LatLng
from report.model.Report import Report
from report.repository.ReportRepository import ReportRepository


class ReportManager:
    def __init__(self, reportRepo: ReportRepository):
        self.reportRepo = reportRepo

    def addReport(self, report: Report):
        self.reportRepo.saveReport(report)

    def getReports(self, location: LatLng) -> List[Report]:
        return self.reportRepo.getReports(location)
