from typing import List

from report.Report import Report
from report.ReportRepository import ReportRepository


class ReportManager:
    def __init__(self, reportRepo: ReportRepository):
        self.reportRepo = reportRepo

    def addReport(self, report: Report):
        self.reportRepo.saveReport(report)

    def getReports(self, location) -> List[Report]:
        return self.reportRepo.getReports(location)
