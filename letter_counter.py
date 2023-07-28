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

fileOne = file("example.txt")
print(fileOne.fileRead())
