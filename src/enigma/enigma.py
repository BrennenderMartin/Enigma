
class Enigma:
    def __init__(
            self,
            text: str,
            datum: str,
            walzenlage: list[str],
            ringstellung: list[int],
            steckerverbindung: list[str],
            kenngruppen: list[str]
        ):
        self.text: str = text
        self.datum: str = datum
        self.walzenlage: list[str] = walzenlage
        self.ringstellung: list[int] = ringstellung
        self.steckerverbindung: list[str] = steckerverbindung
        self.kenngruppen: list[str] = kenngruppen
    
    def encode(self, text: str) -> str:
        steckeredText = self.stecker(text)
        
        # encode with rotors
        
        retText = self.stecker(steckeredText)
        
        return retText
    
    def decode(self, text: str) -> str:
        retText = text
        ...
        return retText
    
    def stecker(self, text: str):
        """
            loops through a whole text and steckers every letter anew
        """
        text = "".join(text.upper().split())
        workList = list(text)
        steckeredText = ""
        for item in workList:
            item = self.steckerbrett(item)
            steckeredText += item
        return steckeredText
    
    def steckerbrett(self, inputChar: str) -> str:
        """
            Takes an input and converts it through the Steckerverbindungen of this enigma machine
        """
        inputChar = inputChar.upper()
        outputChar = inputChar
        for item in self.steckerverbindung:
            for char in item:
                if inputChar == char:
                    item = list(item)
                    for lItem in item:
                        if lItem != inputChar:
                            outputChar = lItem
        return outputChar
    
    def __str__(self) -> str:
        return f"""
{self.text},
{self.datum},
{self.walzenlage},
{self.ringstellung},
{self.steckerverbindung},
{self.kenngruppen}
        """