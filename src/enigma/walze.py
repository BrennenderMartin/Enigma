import json
import string

class Enigma:
    def __init__(self, name: str, vorlage: dict, startingPosition: str):
        self.name: str = name
        self.type = self.name.split("-")
        
        self.walzenlage: list[str] = vorlage["Walzenlage"]
        self.ringstellung: list[int] = vorlage["Ringstellung"]
        self.steckerverbindung: list[str] = vorlage["Steckerverbindung"]
        self.kenngruppen: list[str] = vorlage["Kenngruppen"]
        
        self.startingPositions: list[int] = [
            string.ascii_uppercase.index(char) for char in startingPosition
        ]
        
        self.walzen: list[Walze] = []


    def encode(self, text: str) -> str:
        """
            Runs the whole Enigma: Steckerbrett -> Rotoren -> Steckerbrett
            Converts the returned-joined String into a String with len(5) elements split by spaces
        """
        steckeredText = self.steckerLoop(text)
        
        workText = self.rotors(steckeredText)
        
        retText = self.steckerLoop(workText)
        
        return self.getFiveCharString(retText)


    def getFiveCharString(self, text: str) -> str:
        """
            Takes a joint sting and cuts it into 5 chars long items, seperated by a space in one string
            Example: Dear User Hello World -> DearU serHe lloWo rld
        """
        retText = ""
        for item in [text[i:i+5] for i in range(0, len(text), 5)]:
            retText += f"{item} "
        return retText


    def steckerLoop(self, text: str) -> str:
        """
            Loops through a whole text and steckers every letter a new
        """
        workList = list("".join(text.upper().split()))
        steckeredText = ""
        for item in workList:
            steckeredText += self.steckerSwitch(item)
        return steckeredText


    def steckerSwitch(self, inputChar: str) -> str:
        """
            Takes an input and converts it through the Steckerverbindungen of this enigma machine
        """
        outputChar = inputChar
        for item in self.steckerverbindung:
            for char in item:
                if inputChar == char:
                    for listItem in list(item):
                        if listItem != inputChar:
                            outputChar = listItem
        return outputChar


    def rotors(self, text: str) -> str:
        #Convert startingPositions from the letter to integers
        
        
        #Create the Walzen return [etw, ukw, III, IV, V]
        self.walzen = self.getRotors("rotors.json", self.startingPositions)
        
        #Order, in which the rotors will be gone through
        runOrder = [0, 2, 3, 4, 1, 4, 3, 2, 0]
        
        #List, that has the corresonding int for each letter in the message
        workList: list[int] = [string.ascii_uppercase.index(char) for char in text]
        retList: list[int] = []
        
        print(self.startingPositions)
        print(self.walzen)
        print(workList)
        
        for item in workList:
            for walze in runOrder:
                item = self.walzen[walze].run(item)
            retList.append(item)
            self.rotate()
        
        retText = "".join(string.ascii_uppercase[i] for i in retList)
        return retText


    def rotate(self):
        """
            Lets the first rotor rotate, if it returns true, the next one rotates too, ...
        """
        if self.walzen[2].rotate():
            if self.walzen[3].rotate():
                if self.walzen[4].rotate():
                    pass


    def getRotors(self, referencePath: str, startingPositions: list[int]) -> list[Walze]:
        """
        Docstring für findRotors
        
        :param self: 
        :param referencePath: Pfad der Rotorenliste, welche durchsucht wird
        :type referencePath: str
        :param startingPositions: Startpositionen als liste von integern
        :type startingPositions: list[int]
        :return: Liste der Walzen [etw, ukw, III, IV, V]
        :rtype: list[Walze]
        """
        with open(f"src/enigma/{referencePath}", "r") as file: 
            rotorTable: dict = json.load(file)
        
        walzen: list = []
        
        if self.type[0] == "Enigma" and self.type[1] in ["I", "M3", "M4"]:
            """ Unnecessary, just appends "UKW B" to the Walzenlage and finds the index of it
            # Check if UKW exists, if not append "UKW B"
            hasUkw = any(walze.split(" ")[0] == "UKW" for walze in self.walzenlage)
            if not hasUkw:
                self.walzenlage.append("UKW B")
            
            # Find UKW index
            ukwIndex = next(
                (i for i, walze in enumerate(self.walzenlage) 
                    if walze.split(" ")[0] == "UKW"), -1
            )
            """
            
            for item in rotorTable:
                if item["walze"] == "ETW":
                    etw = Walze(item)
                    walzen.append(etw)
                    
                elif item["walze"] == f"UKW {self.walzenlage[-1]}":
                    ukw = Walze(item)
                    walzen.append(ukw)
                    
                else:
                    for i, walze in enumerate(self.walzenlage):
                        if item["walze"] == walze:
                            walzen.append(Walze(item, startingPositions[i]))
        else:
            print("Unfinished logic! Not yet implemented, please change file for implmentation!")
        
        return walzen


    def __repr__(self) -> str:
        return f"{self.name, self.type, self.walzenlage, self.ringstellung, self.steckerverbindung, self.kenngruppen}"

class Walze:
    def __init__(self, source: dict, start: int = 0):
        self.walzenart: str = source["walze"]
        self.wiring: str = source["wiring"]
        self.encoding: list[int] = self.getEncoding()
        
        if self.walzenart.split(" ")[0] not in ["ETW", "UKW"]:
            self.kerbe: list = string.ascii_uppercase.index(source["kerbe"])
            self.rotierbar: bool = True
        else:
            self.kerbe: list = None
            self.rotierbar: bool = False
        
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
