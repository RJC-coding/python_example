class file:
    def __init__(self, filepath):
        self.filepath=filepath
        
    def fileRead(self):
        counter=0
        file = open(self.filepath, "r")
        for line in file:
            for character in line:
                if (ord(character)>64 and ord(character)<91) or (ord(character)>96 and ord(character)<123):
                    counter+=1
        return "There are " + str(counter) + " letters in "+ self.filepath +"."


class main:
    def getFile(self):
        fileFound=False
        while fileFound==False:
            print("Please enter a filename.")
            filepath = input()
            try:
                fileOne = file(filepath)
                print(fileOne.fileRead())
                fileFound=True
            except:
                print("Could not read this file.")

main = main()
main.getFile()
    
    
