#https://www.w3schools.com/python/python_dictionaries_add.asp
#https://www.programiz.com/python-programming/methods/string/lower
openFile = open("example2.txt","r")
wordDict={}
numbers=[]
punctuation=[" ", ",", ".","?","'","!"]
for line in openFile:
    word=""
    for letter in line:
        if letter!=" ":
            word+=letter
        else:
            if len(word)>0:
                if word[0] in punctuation:
                    word=word[1:len(word)]
                if len(word)>1:
                    if word[len(word)-1] in punctuation:
                        word=word[0:len(word)-1]
                word=word.lower()
                wordNumber=1
                if word in wordDict:
                    wordNumber+=wordDict[word]
                if len(word)>0:
                    wordDict.update({word:wordNumber})
                    word=""
for x in wordDict:
    numbers.append(wordDict[x])
#https://www.w3schools.com/python/ref_list_sort.asp
numbers.sort(reverse=True)
topNumber=numbers[0]
#For words above 1000 times appeared
while topNumber>0:
    for x in wordDict:
        if wordDict[x]==topNumber:
            print(str(x) + " " + str(wordDict[x]))
    topNumber-=1
