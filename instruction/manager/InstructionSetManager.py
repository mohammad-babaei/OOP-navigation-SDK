from typing import List
from instruction.entity.Instruction import Instruction
from instruction.manager.TextToSpeechConverter import TextToSpeechConverter
from instruction.entity.Audio import Audio
from router.entity.Route import Route

class InstructionSetManager:
    
    def __init__(self, instructions: List[Instruction], converter: TextToSpeechConverter):
        self._converter = converter
        self._instructions = instructions

    def getInstructionSet(self):
        return self._instructions

    #the method is mocked
    def setInstructionSet(self, route: Route):
        self._instructions.append(Instruction('001'))
        self._instructions.append(Instruction('101'))

    def getAudioSet(self):
        audioSet = []
        for item in self._instructions:
            audioSet.append(self._converter.convertTextToVoice(instruction=item))
        return audioSet
