from interface import Interface, implements
from instruction.entity.Audio import Audio
from instruction.entity.Instruction import Instruction


class TextToSpeechConverter(Interface):
    def convertTextToVoice(self, instruction: Instruction):
        pass


class PersianConverter(implements(TextToSpeechConverter)):
    #the method is mocked
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio('Be Raast Bepichid')
        return audio


class EnglishConverter(implements(TextToSpeechConverter)):
    #the method is mocked
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio('Turn Right')
        return audio


class ArabicConverter(implements(TextToSpeechConverter)):
    #the method is mocked
    def convertTextToVoice(self, instruction: Instruction):
        audio = Audio('Aneataf Yamina')
        return audio
