from interface import Interface, implements
from instruction.entity.Audio import Audio
from instruction.entity.Instruction import Instruction


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
