animalList=[]

class animal():
    name=""
    description=""

def openFile():
    file = open("animals.csv")
    fileInfo=[]
    for line in file:
        fileInfo.append(line)
    for f in fileInfo:
        if fileInfo.index(f)>0:
            a = animal()
            a.name=f.split(",")[0]
            a.description=f.split(",")[1]
            animalList.append(a)
    file.close()

def searchAnimal(searchTerm):
    for a in animalList:
        if a.name.lower()==searchTerm.lower():
            return animalList.index(a)
    return None

def editAnimal():
    print("Please enter an animal.")
    searchTerm=input()
    result = searchAnimal(searchTerm)
    if (result==None):
        print("Could not find this.")
        return None
    print("Please enter the new description.")
    change=input()
    animalList[result].description=change
    complete=False
    while (complete==False):
        print("Press y to save changes.")
        answer=input()
        if (answer=='y' or answer=='Y'):
            saveChanges()
            complete=True

def saveChanges():
    file = open("animals.csv", "w")
    file.write("Name")
    file.write(",")
    file.write("Description")
    file.write("\n")
    for a in animalList:
        file.write(a.name)
        file.write(",")
        file.write(a.description)
        file.write("\n")
    file.close()

openFile()
editAnimal()
