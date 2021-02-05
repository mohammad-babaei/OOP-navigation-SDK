from interface import Interface, implements
from Instruction import Instruction
from Audio import Audio


class TextToSpeechConverter(Interface):
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio()
        return audio


class PersianConverter(implements(TextToSpeechConverter)):
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio()
        return audio


class EnglishConverter(implements(TextToSpeechConverter)):
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio()
        return audio


class ArabicConverter(implements(TextToSpeechConverter)):
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio()
        return audio
