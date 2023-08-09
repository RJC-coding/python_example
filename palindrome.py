class checker:
    def check(self, word):
        i=0
        j=len(word)-1
        while j!=i:
            if word[i]!=word[j]:
                return False
            i=i+1
            j=j-1
        return True

check = checker()
print("Enter a word to learn if it is a palindrome.")
word = input()
wordNoSpace=word.replace(" ", "")
wordNoSpace=wordNoSpace.replace(",", "")
wordNoSpace=wordNoSpace.replace("'", "")
wordNoSpace=wordNoSpace.replace("\"", "")
wordNoSpace=wordNoSpace.replace(".", "")
wordNoSpace=wordNoSpace.replace("!", "")
print(wordNoSpace)
result = check.check(wordNoSpace)
if result:
    print("Palindrome")
else:
    print("Not a palindrome.")
