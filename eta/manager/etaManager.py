from router.entity.Route import Route
from report.repository.ReportRepository import ReportRepository


class etaManager:
    def __init__(self, reportRepo: ReportRepository, reportData):
        self.reportRepo = reportRepo
        self.reportData = reportData

    def calculateRouteETA(self, route: Route):
        self.reportData = self.getReportData(route)
        pass

    def getReportData(self, route):
        pass
