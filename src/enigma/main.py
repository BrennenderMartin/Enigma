import json
import string
from enigma.enigma import Enigma

"""
What does this Programm need to do:
1. Create a Vorlage, that can be read easily
    1. Parse through the vorlage_vorlage.json
    2. create a new file and for each element insert a new str in the new file
1. OR get the Vorlage for a given day based on a database
    1. Write the Database (yay!)
2. Open a Vorlage, to be able to read and write encrypted files
3. Encrypt a message and save it as a Nachricht
4. Open a Nachricht, to decrypt it
with open("nachricht.json", "r") as file:
    nachricht = json.load(file)
def buildFile(file):
    with open(f"")
print(nachricht)

Iteration over the vorlage.json
for item in vorlage:
    print(f"{item}: ")
    if type(vorlage[item]) == list:
        for lItem in vorlage[item]:
            print(lItem)
    else:
        print(vorlage[item])
        
        
HELLO WORLD

YYWBG YTBIK
"""

def create_enigma(filePath: str, name: str, startingPosition: str):
    with open(f"src/enigma/{filePath}", "r") as file:
        vorlage: dict = json.load(file)
    
    enigma = Enigma(name, vorlage, startingPosition)
    
    print("Output:", enigma.encode("HELLO WORLD"))
    print(enigma)
    
def main():
    print(string.ascii_uppercase.index("Z"))
    #create_enigma("vorlage.json", "Enigma-I", "QWE")

if __name__ == "__main__":
    main()
