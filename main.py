from instruction.manager.InstructionSetManager import InstructionSetManager
from instruction.manager.TextToSpeechConverter import TextToSpeechConverter
from instruction.manager.TextToSpeechConverter import PersianConverter
from router.entity.Route import Route

if __name__ == '__main__':
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