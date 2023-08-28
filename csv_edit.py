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
            a.description=f.split(",")[1].strip()
            animalList.append(a)
    file.close()

def searchAnimal(searchTerm):
    for a in animalList:
        if a.name.lower()==searchTerm.lower():
            return animalList.index(a)
    return None

def editAnimal():
    print("Please enter an animal name.")
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

def addAnimal():
    nameComplete=False
    while (nameComplete==False):
        print("Please enter an animal name.")
        name=input()
        if (len(name)>0):
            nameComplete=True
    descComplete=False
    while (descComplete==False):
        print("Please enter a description.")
        description=input()
        if (len(description)>0):
            descComplete=True
    a = animal()
    a.name=name
    a.description=description
    animalList.append(a)
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
running=True
while(running):
    print("Edit animals: e")
    print("Add animal: a")
    print("Quit: q")
    answer=input()
    if answer=='e':
        editAnimal()
    elif answer=='a':
        addAnimal()
    elif answer=='q':
        running=False
