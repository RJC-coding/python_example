def wordReverse(word):
    array = []
    for i in word:
        array.append(i)
    array.reverse()
    newWord = ""
    for i in array:
        newWord=newWord+i
    return newWord

def main():
    complete=False
    while (complete==False):
        word = ""
        while len(word)==0:
            print("Please enter a word to reverse. Enter q to exit.")
            word=input().strip()
            if (word=="q"):
                complete=True
            else:
                print(wordReverse(word))

main()
