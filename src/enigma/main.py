import json
from pathlib import Path

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
"""

def findRelativePath() -> str:
    currentFile = Path(__file__).resolve()
    # Walk up until we find 'src' in the path
    for parent in currentFile.parents:
        if parent.name == "src":
            projectRoot = parent.parent
            break
    return str(currentFile.parent.relative_to(projectRoot))

def createMaschienenschluessel():
    with open(f"{RelativePath}vorlage.json", "r") as file:
        vorlage = json.load(file)
    
    newFile = {}
    
    print("Please enter A or B for one of the following valid methods:")
    print("A: Input data manually")
    print("B: Input complete string")
    allOrEx = input()
    
    if allOrEx == "A":
        newFile = createMaschienenschluesselManually(vorlage)
    
    elif allOrEx == "B":
        newFile = createMaschienenschluesselFromExample(vorlage)
    
    print(newFile)

def createMaschienenschluesselManually(vorlage):
    newFile = {}
    for item in vorlage:
            if item == "Beispiel":
                continue
            
            elif type(vorlage[item]) == str:
                newFile[item] = input(f"{item}: ")
            
            elif type(vorlage[item]) == list:
                print(f"{item} ({len(vorlage[item])}):")
                itemList = []
                for count, obj in enumerate(vorlage[item]):
                    itemList.append(input(f"{count + 1}: "))
                newFile[item] = itemList
            
            else:
                raise Exception("Invalid type")
    
    return newFile

def createMaschienenschluesselFromExample(vorlage):
    newFile = {}
    print("The following things have to be entererd, seperated by a '-' and individual items with a ' '.")
    for item in vorlage:
            if item == "Beispiel":
                continue
            
            elif type(vorlage[item]) == str:
                print(f"{item},")
            
            elif type(vorlage[item]) == list:
                print(f"{item} ({len(vorlage[item])}),")
    
    keyInput = input("Maschienenschluessel: ")
    key = keyInput.split("-")
    for i, item in enumerate(key):
        key[i] = item.split(" ")
        
        for j, item in enumerate(key[i]):
            if item == "":
                del key[i][j]
    print(key)
    
    for count, item in enumerate(vorlage):
        if item == "Beispiel":
            newFile[item] = keyInput
        elif type(vorlage[item]) == str:
            newFile[item] = key[count][0]
        else:
            newFile[item] = key[count]
    
    return newFile

def main():
    print(findRelativePath())
    createMaschienenschluessel()

RelativePath = findRelativePath() + "/"

if __name__ == "__main__":
    main()