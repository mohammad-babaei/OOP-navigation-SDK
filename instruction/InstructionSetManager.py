from typing import List
from Instruction import Instruction
from TextToSpeechConverter import TextToSpeechConverter
# remember to import Route from router

class InstructionSetManager:
    
    def __init__(self, instructions: List[Instruction], converter: TextToSpeechConverter):
        self._converter = converter
        self._instructions = instructions

    def getInstructionSet(self):
        return self._instructions

    def setInstructionSet(self, route: Route):
        pass

    def getAudioSet(self) -> audio:
        pass
