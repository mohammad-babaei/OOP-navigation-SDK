from typing import List

from mapData.entity.LatLng import LatLng
from report.model.Report import Report, ReportType
from router.entity.Route import Route


class ReportRepository:
    def saveReport(self, report: Report):
        print("report: ", report, " is saved successfully")

    def getReports(self, location) -> List[Report]:
        return [
            Report('2020-10-05:20:15:31', ReportType.Accident, LatLng(51.65465, 37.5465), {"property1": True}),
            Report('2021-12-07:19:14:21', ReportType.Police, LatLng(51.65465, 37.5465), {"property1": False}),
        ]

    def getReportsInRoute(self, route: Route) -> List[Report]:
        pass
