from datetime import timedelta
from typing import List

from report.model.Report import Report
from report.repository.ReportRepository import ReportRepository
from router.entity.Route import Route


class ETAManager:
    def __init__(self):
        self.reportRepository = ReportRepository()

    def calculateRouteETA(self, route: Route) -> timedelta:
        pass

    def _getReportData(self, route: Route) -> List[Report]:
        return self.reportRepository.getReportsInRoute(route)
