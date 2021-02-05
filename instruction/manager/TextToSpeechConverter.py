# from interface import Interface, implements
from instruction.entity.Audio import Audio
from instruction.entity.Instruction import Instruction


class TextToSpeechConverter:
    def convertTextToVoice(self, instruction: Instruction):
        pass


class PersianConverter(TextToSpeechConverter):
    #the method is mocked
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio('Be Raast Bepichid')
        return audio


class EnglishConverter(TextToSpeechConverter):
    #the method is mocked
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio('Turn Right')
        return audio


class ArabicConverter(TextToSpeechConverter):
    #the method is mocked
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio('Aneataf Yamina')
        return audio
