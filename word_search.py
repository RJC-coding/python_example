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
                    if len(word)>0:
                        lineWords.append(word)
                        word=""
            LineInfo = lineInfo(line, lineWords)
            lineList.append(LineInfo)
        return lineList

    def fileSearch(self, searchTerm):
        allLines=[]
        lineList = self.fileRead()
        searchTermList=searchTerm.split()
        if len(searchTermList)==1:
            for lineInfo in lineList:
                for word in lineInfo.lineWords:
                    if searchTermList[0].lower() in word.lower():
                        allLines.append(lineInfo.lineString)
        else:
            print(len(searchTermList))
            #Should do this two lines at a time, leapfrogging
            for lineInfo in lineList:
                twoLinesWords=lineInfo.lineWords
                currentIndex=lineList.index(lineInfo)
                if currentIndex<len(lineList)-1:
                    for w in lineList[currentIndex+1].lineWords:
                        twoLinesWords.append(w)
                    print(twoLinesWords)
                for word in twoLinesWords:
                    if searchTermList[0].lower() == word.lower():
                        index=twoLinesWords.index(word)
                        i=1
                        if (index+i)>len(twoLinesWords)-1:
                            break
                        else:
                            #i will refer to the second word in the searchTermList AND will be added to the index to show the next lineWord along
                            while i<len(searchTermList):
                                if searchTermList[i].lower() != twoLinesWords[index+i].lower():
                                    break
                                else:
                                    allLines.append(lineInfo.lineString)
                                i+=1
        return allLines

class lineInfo:
    lineString=""
    lineWords=[]
    def __init__(self, lineString, lineWords):
        self.lineString=lineString
        self.lineWords=lineWords

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
                        print("\"")
                        for r in result:
                            print(r)
                        print("\"")
                    else:
                        print("Search term is not in file.")
                except:
                    print("Could not find this search term.")
                    break
            except:
                print("Could not read this file.")
            

main = main()
main.getFile()
    
    
