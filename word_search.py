class file:
    def __init__(self, filepath):
        self.filepath=filepath
        
    def fileRead(self):
        file = open(self.filepath, "r")
        wordList=[]
        lineCount=0
        for line in file:
            wordString=""
            for character in line:
                if (ord(character)>64 and ord(character)<91) or (ord(character)>96 and ord(character)<123):
                    wordString=wordString+character
                else:
                    if len(wordString)>0:
                        wordOne = word(wordString, lineCount, len(wordList))
                        wordList.append(wordOne)
                        wordString=""
            lineCount+=1
        return wordList

    def fileSearch(self, searchTerm):
        allLines=[]
        relevantWords=[]
        wordList = self.fileRead()
        searchTermList=searchTerm.split()

        for w in wordList:
            for s in searchTermList:
                if w.wordString.lower()==s.lower():
                    relevantWords.append(w)

        finalWords=[]
        counter=0
        while counter<len(relevantWords):
            testList=relevantWords[counter:len(searchTermList)+counter]
            if len(testList)>1:
                testCounter=1
                while testCounter<len(testList):
                    if (testList[testCounter].wordPosition==(testList[testCounter-1].wordPosition)+1):
                        testListStrings=[]
                        for t in testList:
                            testListStrings.append(t.wordString.lower())
                        if (testListStrings==searchTermList):
                            for t in testList:
                                finalWords.append(t)
                    testCounter+=1
            else:
                for t in testList:
                    finalWords.append(t)
            counter+=1

        file = open(self.filepath, "r")
        lineCount=0
        for line in file:
            sameLineWords=0
            for w in finalWords:
                if w.wordLine==lineCount and sameLineWords==0:
                    sameLineWords+=1
                    allLines.append(line)
            lineCount+=1

        return allLines

class word:
    wordString=""
    wordLine=None
    wordPosition=None
    def __init__(self, wordString, wordLine, wordPosition):
        self.wordString=wordString
        self.wordLine=wordLine
        self.wordPosition=wordPosition

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
                searchTerm = input().strip()
                try:
                    result = fileOne.fileSearch(searchTerm)
                    if (len(result)>0):
                        print("Search term exists in file.")
                        print("\"", end="")
                        for r in result:
                            print(r, end="")
                        print("\"", end="")
                    else:
                        print("Search term is not in file.")
                except:
                    print("Could not find this search term.")
                    break
            except:
                print("Could not read this file.")
            

main = main()
main.getFile()
    
    
