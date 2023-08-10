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

wordString=""
for character in word:
    if (ord(character)>64 and ord(character)<91) or (ord(character)>96 and ord(character)<123):
        wordString=wordString+character.lower()
result = check.check(wordString)
if result:
    print("Palindrome")
else:
    print("Not a palindrome.")
