import string

class Rotor:
    def __init__(self, rotor: str, notch: str):
        self.rotorOut: list[int] = [0 for _ in range(26)]
        self.rotorIn: list[int] = [0 for _ in range(26)]
        self.rotorHead: int = 0
        self.ringHead: int = 0
        self.notch: str = ""
        self.rotate: int = 0
        
        self.setRotor([rotor, notch])
    
    def setRotor(self, rotor: list[str]) -> None:
        self.notch = rotor[1]
        for i in range(26):
            rotorFrom: int = i + 1
            rotorTo: int = string.ascii_uppercase.index(rotor[0].split()[i])
            
            if (rotorFrom < rotorTo):
                self.rotorOut[i] = rotorTo - rotorFrom
            else:
                self.rotorOut[i] = (26 - (rotorFrom - rotorTo)) % 26
            
            self.rotorIn[(i + self.rotorOut[i]) % 26] = self.rotorOut[i]
