import string

class Rotor:
    def __init__(self, rotor: str, notch: str):
        self.rotorOut: list[int] = [0 for _ in range(26)]
        self.rotorIn: list[int] = [0 for _ in range(26)]
        self.rotorHead: int = 0
        self.ringHead: int = 0
        self.notch: str = ""
        self.rotated: int = 0
        
        self.setRotor([rotor, notch])
    
    def getOutputOf(self, pos: int) -> int:
        if (self.rotorHead >= self.ringHead):
            rotorRingDiff: int = self.rotorHead - self.ringHead
        else:
            rotorRingDiff = 26 - self.ringHead + self.rotorHead
        return (pos + self.rotorOut[(pos + self.rotated + rotorRingDiff) % 26]) % 26
    
    def getInputOf(self, pos: int) -> int:
        if (self.rotorHead >= self.ringHead):
            rotorRingDiff: int = self.rotorHead - self.ringHead
        else:
            rotorRingDiff = 26 - self.ringHead + self.rotorHead
        
        posJump: int = pos - self.rotorIn[(pos + self.rotated + rotorRingDiff) % 26]
        
        if (posJump > 0):
            return posJump % 26
        else:
            return (26 + posJump) % 26
    
    def getNotch(self) -> str:
        return self.notch
    
    def getRotorHead(self) -> str:
        return string.ascii_uppercase[1 + (self.ringHead + self.rotated) % 26]
    
    def rotate(self) -> None:
        self.rotated = (self.rotated + 1) % 26
    
    def setRotorHead(self, char: str) -> None:
        if (char not in string.ascii_uppercase):
            raise KeyError
        self.rotorHead = string.ascii_uppercase.index(char) - 1
        self.rotated = 0
    
    def setRotor(self, rotor: list[str]) -> None:
        self.notch = rotor[1]
        for i in range(26):
            rotorFrom: int = i + 1
            rotorTo: int = string.ascii_uppercase.index(list(rotor[0])[i])
            
            if (rotorFrom < rotorTo):
                self.rotorOut[i] = rotorTo - rotorFrom
            else:
                self.rotorOut[i] = (26 - (rotorFrom - rotorTo)) % 26
            
            self.rotorIn[(i + self.rotorOut[i]) % 26] = self.rotorOut[i]
