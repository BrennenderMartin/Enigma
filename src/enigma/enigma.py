import json
import string
from enigma.rotor import Rotor
from enigma.reflector import Reflector


class Enigma:
    def __init__(self, left: list[str] = None, center: list[str] = None, right: list[str] = None, ref: str = None):
        self.plugboard: list[int] = [-1 for _ in range(26)]

        self.leftRotor: Rotor  = Rotor(left[0], left[1].strip())
        self.centerRotor: Rotor  = Rotor(center[0], center[1].strip())
        self.rightRotor: Rotor  = Rotor(right[0], right[0].strip())
        self.reflector: Reflector  = Reflector(ref)
    
    def type(self, text: str) -> str:
        output: str = ""
        for char in text:
            if (0 <= string.ascii_uppercase.index(char) <= 25):
                output += self.rotorsEncryption(char)
        
        return output
    
    def rotorsEncryption(self, char: str) -> str:
        return string.ascii_lowercase[string.ascii_uppercase.index(char)]
