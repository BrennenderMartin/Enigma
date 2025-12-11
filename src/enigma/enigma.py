import json

class Enigma:
    def __init__(self, name: str, vorlage: dict):
        self.name: str = name
        self.type = self.name.split("-")
        
        self.vorlage: dict = vorlage
        
        self.walzenlage: list[str] = vorlage["Walzenlage"]
        self.ringstellung: list[int] = vorlage["Ringstellung"]
        self.steckerverbindung: list[str] = vorlage["Steckerverbindung"]
        self.kenngruppen: list[str] = vorlage["Kenngruppen"]
    
    def encode(self, text: str) -> str:
        steckeredText = self.stecker(text)
        
        workText = self.rotors(steckeredText)
        
        #retText = self.stecker(workText)
        
        return workText
    
    def decode(self, text: str) -> str:
        retText = text
        ...
        return retText
    
    def stecker(self, text: str) -> str:
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
    
    def rotors(self, text: str):
        etw, ukw, rotors = self.findRotors()
        #print(f"'\n{repr(etw)},\n\n{repr(ukw)},\n\n{rotors}\n'")
        retText = list(text)
        #print(retText)
        
        #pls just do the logic to make the rotors work and dont just procrastinate!!
        
        return retText

    def findRotors(self) -> list:
        with open(f"src/enigma/rotors.json", "r") as file:
            rotorTable: dict = json.load(file)
        
        walzen: list = []
        if self.type[0] == "Enigma" and self.type[1] in ["1", "M3", "M4"]:
            
            # Check if UKW exists, if not append "UKW B"
            has_ukw = any(walze.split(" ")[0] == "UKW" for walze in self.walzenlage)
            if not has_ukw:
                self.walzenlage.append("UKW B")
            
            # Find UKW index
            ukw_index = next(
                (i for i, walze in enumerate(self.walzenlage) 
                    if walze.split(" ")[0] == "UKW"), -1
            )
            
            for item in rotorTable:
                #Eintrittswalze
                if item["walze"] == "ETW":
                    etw = Walze(item)
                
                #Umkehrwalze
                elif item["walze"] == self.walzenlage[ukw_index]:
                    ukw = Walze(item)
                
                #Hauptwalzen
                else:
                    for walze in self.walzenlage:
                        if item["walze"] == walze:
                            walzen.append(Walze(item))
        else:
            print("Unfinished logic! Not yet implemented, please change file for implmentation!")
        
        walzen.reverse()
        return etw, ukw, walzen
    
    def __repr__(self) -> str:
        return f"{self.name, self.walzenlage, self.ringstellung, self.steckerverbindung, self.kenngruppen}"

class Walze:
    def __init__(self, source: dict):
        self.walzenart: str = source["walze"]
        self.wiring: str = source["wiring"]
        
        if self.walzenart.split(" ")[0] not in ["ETW", "UKW"]:
            self.kerbe: list = source["kerbe"]
        else:
            self.kerbe = None
        
        self.modell: list = source["modell"]
    
    def __str__(self) -> str: 
        return f"{self.walzenart} mit Verkabelung: {self.wiring} und Kerben: {self.kerbe} für Modelle: {self.modell}"
    def __repr__(self) -> str:
        return f"{self.walzenart, self.wiring, self.kerbe, self.modell}"
