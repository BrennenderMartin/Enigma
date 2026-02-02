import string

class Walze:
    def __init__(self, source: dict, start: int):
        self.walzenart: str = source["walze"]
        self.wiring: str = source["wiring"]
        self.encoding: list[int] = self.getEncoding()
        
        if self.walzenart.split(" ")[0] not in ["ETW", "UKW"]:
            self.kerbe: list = source["kerbe"]
            self.startPosition: int = start
        else:
            self.kerbe = None
            self.startPosition = 0
        
        self.modell: list = source["modell"]
    
    def getEncoding(self) -> str:
        encoding: list[int] = []
        
        for index, item in enumerate(self.wiring):
            encoding.append(string.ascii_uppercase.index(item) - index)
        
        return encoding
    
    def run(self, item: str, index: int) -> str:
        itemIndex = string.ascii_uppercase.index(item)
        movement = self.encoding[itemIndex]
        movedItem = string.ascii_uppercase[itemIndex + movement]
        #print(f"{self.walzenart}:\n{item = }\n{itemIndex = }\n{movement = }\n{movedItem = }\n")
        print(index)
        return movedItem
    
    """ def __str__(self) -> str: 
        return f"{self.walzenart} mit Verkabelung: {self.wiring} und Kerben: {self.kerbe} für Modelle: {self.modell}"
    """
    
    def __repr__(self) -> str:
        return f"{self.walzenart, self.wiring, self.kerbe, self.modell}"
