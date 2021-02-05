from typing import List

from report.model.Report import Report
from router.entity.Route import Route


class ReportRepository:
    def saveReport(self, report: Report):
        pass

    def getReports(self, location) -> List[Report]:
        pass

    def getReportsInRoute(self, route: Route) -> List[Report]:
        pass
