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
    word = ""
    while len(word)==0:
        print("Please enter a word to reverse")
        word=input().strip()
    print(wordReverse(word))

main()
