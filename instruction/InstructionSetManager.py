from typing import List
from Instruction import Instruction
from TextToSpeechConverter import TextToSpeechConverter
from Audio import Audio
# remember to import Route from router

class InstructionSetManager:
    
    def __init__(self, instructions: List[Instruction], converter: TextToSpeechConverter):
        self._converter = converter
        self._instructions = instructions

    def getInstructionSet(self):
        return self._instructions

    def setInstructionSet(self, route: Route):
        pass

    def getAudioSet(self):
        audioSet = []
        for item in self._instructions:
            audioSet.append(self._converter.convertTextToVoice(instruction=item))
        return audioSet
