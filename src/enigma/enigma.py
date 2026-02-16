import json
import string
from enigma.rotor import Rotor
from enigma.reflector import Reflector


class Enigma:
    def __init__(self, left: list[str], center: list[str], right: list[str], ref: str):
        plugboard: list[int] = [-1 for _ in range(26)]
        
        #Make getter logic for that
        I = {"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"}
        II = {"AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"}
        III = {"BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"}
        IV = {"ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"}
        V = {"VZBRGITYUPSDNHLXAWMJQOFECK", "Z"}
    
        A = "EJMZALYXVBWFCRQUONTSPIKHGD"
        B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

        leftRotor: Rotor  = Rotor(left[0], left[1].strip())
        centerRotor: Rotor  = Rotor(center[0], center[1].strip())
        rightRotor: Rotor  = Rotor(right[0], right[0].strip())
        reflector: Reflector  = Reflector(ref)
    
    def type(self, text: str) -> str:
        output: str = ""
        for char in text:
            if (0 <= string.ascii_uppercase.index(char) <= 25):
                output += self.rotorsEncryption(char)
    
    def rotorsEncryption(self, char: str) -> str:
        ...
