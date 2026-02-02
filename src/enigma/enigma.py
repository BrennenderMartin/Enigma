import json
import string
from enigma.walze import Walze

class Enigma:
    def __init__(self, name: str, vorlage: dict):
        self.name: str = name
        self.type = self.name.split("-")
        
        self.vorlage: dict = vorlage
        
        self.walzenlage: list[str] = vorlage["Walzenlage"]
        self.ringstellung: list[int] = vorlage["Ringstellung"]
        self.steckerverbindung: list[str] = vorlage["Steckerverbindung"]
        self.kenngruppen: list[str] = vorlage["Kenngruppen"]
        
        self.walzen: list[Walze] = []
    
    
    def encode(self, text: str, startingPosition: str) -> str:
        steckeredText = self.stecker(text)
        
        workText = self.rotors(steckeredText, startingPosition)
        
        retText = self.stecker(workText)
        
        return self.getEnigmaString(retText)
    
    
    def decode(self, text: str) -> str:
        retText = text
        ...
        return retText
    
    
    def getEnigmaString(self, text: str) -> str:
        """
        Takes a joint sting and cuts it into 5 chars long items, seperated by a space in one string
        Example: Dear User Hello World -> DearU serHe lloWo rld
        """
        retText = ""
        for item in [text[i:i+5] for i in range(0, len(text), 5)]:
            retText += f"{item} "
        return retText
    
    
    def stecker(self, text: str) -> str:
        """
            loops through a whole text and steckers every letter a new
        """
        workList = list("".join(text.upper().split()))
        steckeredText = ""
        for item in workList:
            steckeredText += self.steckerbrett(item)
        return steckeredText
    
    
    def steckerbrett(self, inputChar: str) -> str:
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


    def rotors(self, text: str, startingPosition: str) -> str:
        startingPositions: list = []
        for item in startingPosition:
            startingPositions.append(string.ascii_uppercase.index(item))
        self.walzen = self.findRotors("rotors.json", startingPositions)
        
        runOrder = [0, 2, 3, 4, 1, 4, 3, 2, 0]
        workList: list[int] = [string.ascii_uppercase.index(char) for char in text]
        
        print(startingPositions)
        print(self.walzen)
        print(workList)
        
        """
        print("Items:\n")
        for index, item in enumerate(workList):
            #for walze in runOrder:
                #item = walzen[walze].run(item, index)
            print("")
        
        
        for walze in walzen:
            print(walze.walzenart, walze.encoding)
        """
        
        retText = "".join(string.ascii_uppercase[i] for i in workList)
        return retText


    def findRotors(self, referencePath: str, startingPositions: list[int]) -> list[Walze]:
        with open(f"src/enigma/{referencePath}", "r") as file: # referencePath meint hier die Rotorenliste (path)
            rotorTable: dict = json.load(file)
        
        walzen: list = []
        
        if self.type[0] == "Enigma" and self.type[1] in ["1", "M3", "M4"]:
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
        return f"{self.name, self.walzenlage, self.ringstellung, self.steckerverbindung, self.kenngruppen}"
