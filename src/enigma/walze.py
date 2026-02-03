import string

class Walze:
    def __init__(self, source: dict, start: int = 0):
        self.walzenart: str = source["walze"]
        self.wiring: str = source["wiring"]
        self.encoding: list[int] = self.getEncoding()
        
        if self.walzenart.split(" ")[0] not in ["ETW", "UKW"]:
            self.kerbe: list = string.ascii_uppercase.index(source["kerbe"])
            self.rotierbar: bool = True
        else:
            self.kerbe = None
            self.rotierbar = False
        
        self.position: int = start
        self.modell: list = source["modell"]
    
    
    def getEncoding(self) -> list[int]:
        """
        Docstring für getEncoding
        
        :param self: Beschreibung
        :return: Beschreibung
        :rtype: str
        """
        encoding: list[int] = []
        
        for index, item in enumerate(self.wiring):
            encoding.append(string.ascii_uppercase.index(item) - index)
        
        return encoding
    
    
    def rotate(self) -> bool:
        print(f"{self.walzenart} rotiert!")
        self.position = (self.position + 1) % 26
        if self.position == self.kerbe: return True
        else: return False
    
    
    def run(self, item: int) -> int:
        #itemIndex = string.ascii_uppercase.index(item)
        #movement = self.encoding[itemIndex]
        #movedItem = string.ascii_uppercase[itemIndex + movement]
        #print(f"{self.walzenart}:\n{item = }\n{itemIndex = }\n{movement = }\n{movedItem = }\n")
        #print(index)
        retItem = (item + self.encoding[(item + self.position) % 26]) % 26
        print(f"{self.walzenart=}, {item=}, {retItem=}")
        return retItem
    
    
    """ def __str__(self) -> str: 
        return f"{self.walzenart} mit Verkabelung: {self.wiring} und Kerben: {self.kerbe} für Modelle: {self.modell}"
    """
    
    def __repr__(self) -> str:
        return f"{self.walzenart, self.wiring, self.kerbe, self.modell}"
