from instruction.manager.InstructionSetManager import InstructionSetManager
from instruction.manager.TextToSpeechConverter import PersianConverter
from mapData.entity.LatLng import LatLng
from mapData.manager.MapDataManager import MapDataManager
from mapData.repository.MapDataRepository import MapDataRepository
from report.manager.ReportManager import ReportManager
from report.model.Report import Report, ReportType
from report.repository.ReportRepository import ReportRepository
from router.entity.Route import Route
from router.manager.RoutingManager import Router
from router.manager.ShortestPathAlgorithm import Dijkstra

if __name__ == '__main__':
    print('________________________running_report_start_________________\n')
    reportRepository = ReportRepository()

    reportManager = ReportManager(reportRepository)

    reportInstance = Report('2020-10-05:20:15:31', ReportType.Accident, LatLng(51.65465, 37.5465),
                            {"property1": True})

    reportManager.addReport(reportInstance)

    reports = reportManager.getReports(LatLng(51.65465, 37.5465))

    print('fetched reports are:', reports)

    print('\n________________________running_report_end_________________\n')

    print('________________________running_router_start_________________\n')
    # instantiating MapDataRepository and MapDataManager
    mapDataRepository = MapDataRepository()
    mapDataManager = MapDataManager(mapDataRepository)

    # instantiating Router
    router = Router(Dijkstra(), mapDataManager)

    shortestPathRoute = router.findShortestPath(LatLng(51.65465, 37.5465), LatLng(63.65465, 40.5465))

    print("calculated shortest path is: ", shortestPathRoute)

    print('\n________________________running_router_end_________________\n')

    converter = PersianConverter()
    manager = InstructionSetManager(instructions=[], converter=converter)

    ways = []
    route = Route(ways=ways)

    manager.setInstructionSet(route=route)
    instructionSet = manager.getInstructionSet()
    audioSet = manager.getAudioSet()

    print(instructionSet[0].getText())
    print(instructionSet[1].getText())
    print(audioSet[0])
    print(audioSet[1])
