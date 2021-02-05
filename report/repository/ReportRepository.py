from typing import List

from report.model.Report import Report


class ReportRepository:
    def saveReport(self, report: Report):
        pass

    def getReports(self, location) -> List[Report]:
        pass
