import json

def createMaschienenschluessel():
    with open("src/enigma/vorlage.json", "r") as file:
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
    createMaschienenschluessel()

if __name__ == "__main__":
    main()
