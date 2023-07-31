class file:
    def __init__(self, filepath):
        self.filepath=filepath
        
    def fileRead(self):
        lineList=[]
        file = open(self.filepath, "r")
        for line in file:
            lineWords=[]
            word=""
            for character in line:
                if (ord(character)>64 and ord(character)<91) or (ord(character)>96 and ord(character)<123):
                    word=word+character
                else:
                    lineWords.append(word)
                    word=""
            lineList.append(lineWords)
        return lineList

    def fileSearch(self, searchTerm):
        lineList = self.fileRead()
        for line in lineList:
            for word in line:
                if word.lower()==searchTerm.lower():
                    return line
        return None
        

class main:
    def getFile(self):
        fileFound=False
        while fileFound==False:
            print("Please enter a filename.")
            filepath = input()
            try:
                fileOne = file(filepath)
                fileFound=True
                print("Please enter a search term.")
                searchTerm = input()
                try:
                    result = fileOne.fileSearch(searchTerm)
                    if (len(result)>0):
                        print("Search term exists in file.")
                        print(result)
                    else:
                        print("Search term not in file.")
                except:
                    print("Could not find this search term.")
                    break
            except:
                print("Could not read this file.")
            

main = main()
main.getFile()
    
    
