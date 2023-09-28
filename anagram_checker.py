class check():
    def check(self, first, second):
        cleanedFirst=""
        cleanedSecond=""
        first=first.lower()
        second=second.lower()
        for f in first:
            if ord(f)>96 and ord(f)<123:
                cleanedFirst=cleanedFirst+f
        for s in second:
            if ord(s)>96 and ord(s)<123:
                cleanedSecond=cleanedSecond+s
        if sorted(cleanedFirst)==sorted(cleanedSecond):
            print("Anagram")

complete=False

print("Press q to exit.")
while (complete==False):
    check = check()
    print("Enter first phrase")
    first= input()
    if (first=="q"):
        complete=True
    else:
        print("Enter second phrase")
        second= input()
        if (second=="q"):
            complete=True
        else:
            check.check(first, second)
